import assert from "node:assert/strict";
import test from "node:test";
import { normalize, sparkline, summarize } from "../src/index.js";

test("normalize maps values into the 0..1 range", () => {
  assert.deepEqual(normalize([10, 20, 30]), [0, 0.5, 1]);
});

test("normalize handles flat series", () => {
  assert.deepEqual(normalize([7, 7, 7]), [0, 0, 0]);
});

test("sparkline returns one glyph per input", () => {
  assert.equal(sparkline([1, 2, 3, 4]).length, 4);
  assert.equal(sparkline([1, 2, 3, 4]), "▁▃▆█");
});

test("summarize reports series metadata", () => {
  assert.deepEqual(summarize([4, 2, 9]), {
    count: 3,
    min: 2,
    max: 9,
    latest: 9,
  });
});

test("invalid values throw", () => {
  assert.throws(() => normalize([1, Number.NaN]), /finite numbers/);
});
