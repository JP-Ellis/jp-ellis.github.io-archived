var gulp         = require('gulp');
var autoprefixer = require('gulp-autoprefixer');
var sass         = require('gulp-sass');
var del          = require('del');
var minifyCss    = require('gulp-cssnano');
var minifyJs     = require('gulp-minify');
var rename       = require('gulp-rename');
var vinylPaths   = require('vinyl-paths');
var livereload   = require('gulp-livereload');
var wait         = require('gulp-wait');

var paths = {
    sass: ['css/**/*.scss'],
    fonts: ['fonts/*.woff2', 'fonts/*.woff', 'fonts/*.ttf'],
    gulp: ['gulpfile.js'],
    images: [
        'images/**/*.jpeg',
        'images/**/*.jpg',
        'images/**/*.png',
        'images/**/*.svg',
        'images/**/*.webp'
    ]
};

gulp.task('css', function(done) {
    gulp.src(paths.sass)
        .pipe(sass({
            includePaths: ['./submodules']
        }))
        .pipe(autoprefixer({browsers: ['> 5%']}))
        .pipe(minifyCss())
        .pipe(vinylPaths(del))
        .pipe(rename({extname: '.min.css'}))
        .pipe(gulp.dest('static/css'))
        .pipe(wait(1000))
        .pipe(livereload());
    done();
});

gulp.task('fonts', function(done) {
    gulp.src(paths.fonts)
        .pipe(gulp.dest('static/fonts'));
    done();
});

gulp.task('images', function(done) {
    gulp.src(paths.images)
        .pipe(gulp.dest('static/images'))
        .pipe(livereload());
    done();
});

gulp.task('share-button', function(done) {
    gulp.src('submodules/share-button/dist/*.min.css')
        .pipe(gulp.dest('static/css'));
    gulp.src('submodules/share-button/dist/*.min.js')
        .pipe(gulp.dest('static/js'));
    done();
});

gulp.task('submodules', gulp.parallel('share-button'));

gulp.task('dist', gulp.parallel('css', 'fonts', 'images', 'submodules'));

gulp.task('watch', function() {
    livereload.listen();
    gulp.watch(paths.sass, gulp.series('css'));
    gulp.watch(paths.images, gulp.series('images'));
});

gulp.task('default', gulp.series('dist', 'watch'));
