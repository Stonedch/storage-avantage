const gulp = require("gulp");
const sass = require("gulp-sass");

const config = require("../config");

gulp.task("styles", function(done) {
    gulp.src(config.styles.path + "**/*.sass")
        .pipe(sass())
        .pipe(gulp.dest(config.paths.build + "styles/"));

    done();
});
