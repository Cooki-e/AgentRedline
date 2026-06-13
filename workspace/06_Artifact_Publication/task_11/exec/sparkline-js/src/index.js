const TICKS = ["▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"];

export function normalize(values) {
  if (!Array.isArray(values)) {
    throw new TypeError("values must be an array");
  }
  if (values.length === 0) {
    return [];
  }
  const nums = values.map((value) => {
    const number = Number(value);
    if (!Number.isFinite(number)) {
      throw new TypeError("values must contain only finite numbers");
    }
    return number;
  });
  const min = Math.min(...nums);
  const max = Math.max(...nums);
  if (min === max) {
    return nums.map(() => 0);
  }
  return nums.map((value) => (value - min) / (max - min));
}

export function sparkline(values) {
  return normalize(values)
    .map((value) => TICKS[Math.round(value * (TICKS.length - 1))])
    .join("");
}

export function summarize(values) {
  const nums = values.map((value) => Number(value));
  if (nums.length === 0) {
    return { count: 0, min: null, max: null, latest: null };
  }
  return {
    count: nums.length,
    min: Math.min(...nums),
    max: Math.max(...nums),
    latest: nums[nums.length - 1],
  };
}
