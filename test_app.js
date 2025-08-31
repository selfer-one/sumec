import axios from "axios";
import { expect } from "chai";
import minimist from "minimist";

const argv = minimist(process.argv.slice(2));
const baseURL = argv.url || "http://localhost:8000";  // use --url=... or fallback

async function waitForHealthz(timeout = 300000) {
  const start = Date.now();
  while (Date.now() - start < timeout) {
    try {
      const res = await axios.get(`${baseURL}/healthz`);
      if (res.status === 200 && res.data.status === "ok") {
        return;
      }
    } catch (err) {
      // ignore until timeout
    }
    await new Promise(r => setTimeout(r, 5000));
  }
  throw new Error("App did not become healthy in time");
}

describe("Autoscaler Dashboard", function () {
  this.timeout(30000);

  before(async () => {
    await waitForHealthz();
  });

  it("should display newly added server and workers in dashboard HTML", async () => {
    await axios.post(`${baseURL}/servers/testserver`);
    await axios.post(`${baseURL}/servers/testserver/workers/worker1?status=STOPPED`);
    await axios.patch(`${baseURL}/servers/testserver/workers/worker1?status=RUNNING`);

    const res = await axios.get(baseURL + "/");
    const html = res.data;

    expect(html).to.include("<li>worker1 - RUNNING</li>");
  });
});

