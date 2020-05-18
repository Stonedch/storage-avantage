const gulp = require("gulp");
const browserSync = require("browser-sync").create();

const config = require("../config");
const build = require("./build");

function watch(done) {
    gulp.watch(config.templates.path + "**/*.pug")
        .on("change", gulp.series("build:templates", browserSync.reload));
    gulp.watch(config.styles.path + "**/*.sass")
        .on("change", gulp.series("build:styles", browserSync.reload));
    gulp.watch(config.scripts.path + "**/*.js")
        .on("change", gulp.series("build:scripts", browserSync.reload));
    gulp.watch(config.images.path + "**/*")
        .on("change", gulp.series("build:images", browserSync.reload));

    done();
}

function serve(done) {
    browserSync.init(config.serve);

    done();
}

gulp.task("serve:watch", watch);
gulp.task("serve:serve", gulp.series(
    "build:build",
    gulp.parallel(watch, serve)
));
