const gulp = require("gulp");

const templates = require("./gulp/tasks/templates");
const styles = require("./gulp/tasks/styles");
const scripts = require("./gulp/tasks/scripts");
const images = require("./gulp/tasks/images");
const serve = require("./gulp/tasks/serve");

gulp.task("build", gulp.series(
    "templates:build", "styles:build",
    "scripts:build", "images:build"
));
