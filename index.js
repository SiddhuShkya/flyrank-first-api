const express = require("express");
const app = express();

app.get("/", (req, res) => {
    res.json({ message: "Hello, FlyRank!" });
});

app.get("/status", (req, res) => {
    res.json({ status: "ok", service: "my-first-api" });
});

app.listen(5000, () => console.log("Server running on port 5000"));