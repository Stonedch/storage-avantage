const gulp = require("gulp");

const templates = require("./builds/templates");
const styles = require("./builds/styles");
const scripts = require("./builds/scripts");
const images = require("./builds/images");

gulp.task("build:build", gulp.series(
    "build:templates",
    "build:styles",
    "build:scripts",
    "build:images"
));
