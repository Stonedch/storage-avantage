const gulp = require("gulp");
const rename = require("gulp-rename");

const build = require("./gulp/tasks/build");
const serve = require("./gulp/tasks/serve");
const config = require("./gulp/config");

gulp.task("collect:collect", function(done) {
    gulp.src(config.paths.build + "**/*.html")
        .pipe(rename({suffix: ".new"}))
        .pipe(gulp.dest("../templates/storage/"));
    gulp.src(config.paths.build + "**/*.css")
        .pipe(rename({suffix: ".new"}))
        .pipe(gulp.dest("../static/storage/"));
    gulp.src(config.paths.build + "**/*.js")
        .pipe(rename({suffix: ".new"}))
        .pipe(gulp.dest("../static/storage/"));
    gulp.src(config.paths.build + "images/**/*")
        .pipe(gulp.dest("../static/storage/images/"));

    done();

});
gulp.task("default", gulp.series("build:build"))
