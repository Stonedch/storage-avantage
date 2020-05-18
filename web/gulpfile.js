const gulp = require("gulp");

const build = require("./gulp/tasks/build");
const serve = require("./gulp/tasks/serve");

gulp.task("default", gulp.series("build:build"))
