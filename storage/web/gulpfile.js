const gulp = require("gulp");

const build = require("./gulp/tasks/build");
const serve = require("./gulp/tasks/serve");
const config = require("./gulp/config");

gulp.task("collect:collect", function(done) {
    gulp.src(config.paths.build + "**/*.html")
        .pipe(gulp.dest("../templates/storage/"));
    gulp.src(config.paths.build + "**/*.css")
        .pipe(gulp.dest("../static/storage/"));
    gulp.src(config.paths.build + "**/*.js")
        .pipe(gulp.dest("../static/storage/"));
    gulp.src(config.paths.build + "images/**/*")
        .pipe(gulp.dest("../static/storage/images/"));

    done();

});
gulp.task("default", gulp.series("build:build"))
