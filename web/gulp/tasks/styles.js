const gulp = require("gulp");
const sass = require("gulp-sass");

const config = require("../config");

function styles(done) {
    gulp.src(config.styles.path + "**/*.sass")
        .pipe(sass())
        .pipe(gulp.dest(config.paths.build + "styles/"));

    done();
}

gulp.task("styles", styles);
