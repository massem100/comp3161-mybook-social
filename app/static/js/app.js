$(document).ready(function () {

    'use strict';

    

    // ------------------------------------------------------- //
    // Search Box
    // ------------------------------------------------------ //
    $('#search').on('click', function (e) {
        e.preventDefault();
        $('.search-box').fadeIn();
    });
    $('.dismiss').on('click', function () {
        $('.search-box').fadeOut();
    });

    // ------------------------------------------------------- //
    // Card Close
    // ------------------------------------------------------ //
    $('.card-close a.remove').on('click', function (e) {
        e.preventDefault();
        $(this).parents('.card').fadeOut();
    });

    // ------------------------------------------------------- //
    // Tooltips init
    // ------------------------------------------------------ //    

    $('[data-toggle="tooltip"]').tooltip()


    // ------------------------------------------------------- //
    // Adding fade effect to dropdowns
    // ------------------------------------------------------ //
    $('.dropdown').on('show.bs.dropdown', function () {
        $(this).find('.dropdown-menu').first().stop(true, true).fadeIn();
    });
    $('.dropdown').on('hide.bs.dropdown', function () {
        $(this).find('.dropdown-menu').first().stop(true, true).fadeOut();
    });


    // ------------------------------------------------------- //
    // Sidebar Functionality
    // ------------------------------------------------------ //
    $('#toggle-btn').on('click', function (e) {
        e.preventDefault();
        $(this).toggleClass('active');

        $('.side-navbar').toggleClass('shrinked');
        $('.content-inner').toggleClass('active');
        $(document).trigger('sidebarChanged');

        if ($(window).outerWidth() > 1183) {
            if ($('#toggle-btn').hasClass('active')) {
                $('.navbar-header .brand-small').hide();
                $('.navbar-header .brand-big').show();
            } else {
                $('.navbar-header .brand-small').show();
                $('.navbar-header .brand-big').hide();
            }
        }

        if ($(window).outerWidth() < 1183) {
            $('.navbar-header .brand-small').show();
        }
    });

    // ------------------------------------------------------- //
    // Universal Form Validation
    // ------------------------------------------------------ //

    $('.form-validate').each(function () {
        $(this).validate({
            errorElement: "div",
            errorClass: 'is-invalid',
            validClass: 'is-valid',
            ignore: ':hidden:not(.summernote, .checkbox-template, .form-control-custom),.note-editable.card-block',
            errorPlacement: function (error, element) {
                // Add the `invalid-feedback` class to the error element
                error.addClass("invalid-feedback");
                console.log(element);
                if (element.prop("type") === "checkbox") {
                    error.insertAfter(element.siblings("label"));
                }
                else {
                    error.insertAfter(element);
                }
            }
        });

    });

    // ------------------------------------------------------- //
    // Material Inputs
    // ------------------------------------------------------ //

    var materialInputs = $('input.input-material');

    // activate labels for prefilled values
    materialInputs.filter(function () { return $(this).val() !== ""; }).siblings('.label-material').addClass('active');

    // move label on focus
    materialInputs.on('focus', function () {
        $(this).siblings('.label-material').addClass('active');
    });

    // remove/keep label on blur
    materialInputs.on('blur', function () {
        $(this).siblings('.label-material').removeClass('active');

        if ($(this).val() !== '') {
            $(this).siblings('.label-material').addClass('active');
        } else {
            $(this).siblings('.label-material').removeClass('active');
        }
    });

    // ------------------------------------------------------- //
    // Footer 
    // ------------------------------------------------------ //   

    var contentInner = $('.content-inner');

    $(document).on('sidebarChanged', function () {
        adjustFooter();
    });

    $(window).on('resize', function () {
        adjustFooter();
    })

    function adjustFooter() {
        var footerBlockHeight = $('.main-footer').outerHeight();
        contentInner.css('padding-bottom', footerBlockHeight + 'px');
    }

    // ------------------------------------------------------- //
    // External links to new window
    // ------------------------------------------------------ //
    $('.external').on('click', function (e) {

        e.preventDefault();
        window.open($(this).attr("href"));
    });

    // ------------------------------------------------------- //
    // Text_Posts characters left feature
    // ------------------------------------------------------ //
    $('#characterLeft').text('140 characters left');
    
    $('#message').keyup(function () {
        var max = 140;
        var len = $(this).val().length;
        var ch = max - len;
        if (len >= max) {
            $('#characterLeft').text(-ch +' ' + 'words over the limit');
            $('#characterLeft').addClass('red');
            $('#btnSubmit').addClass('disabled');
        }
        else {
            var ch = max - len;
            $('#characterLeft').text(ch + ' characters left');
            $('#btnSubmit').removeClass('disabled');
            $('#characterLeft').removeClass('red');
        }
    });    

    $('#characterRemaining').text('150 characters left');
    $('#caption').keyup(function () {
        var max = 150;
        var len = $(this).val().length;
        var ch = max - len;
        if (len >= max) {
            $('#characterRemaining').text(-ch + ' ' + 'words over the limit');
            $('#characterRemaining').addClass('red');
            $('#btnSubmit').addClass('disabled');
        }
        else {
            var ch = max - len;
            $('#characterRemaining').text(ch + ' characters left');
            $('#btnSubmit').removeClass('disabled');
            $('#characterRemaining').removeClass('red');
        }
    });    
   
    let posts = document.getElementsByClassName("anch");

    let btns = document.getElementsByClassName("commentbtn");
    // console.log(post_id);
    let index = document.getElementById("index");

    
   
    $('.commentbtn').on('click', function (e) {
        let index = document.getElementById("index");       
        console.log(index.textContent);


        // console.log(post_id);
        // for (var i = 0, l = posts.length; i < l; i++) {
        //     if (posts[i].id == btns[i].id ){
        //         let post_id = posts[i].id;
        //         console.log(post_id);
        //         // console.log(btns[i].id);
                
        //         e.preventDefault();    
        //   }

                
        //}
        let self = this;
        let CommentForm = document.getElementById('CommentForm');
        let form_data = new FormData(CommentForm);
        fetch("/dashboard/<post_id>/comments", {
            method: 'POST',
            body: post_id,
            headers: {
                'X-CSRFToken': token
            },
            credentials: 'same-origin'

        })
            .then(function (response) {
                return response.json();
            })
            .then(function (jsonResponse) {
                // display a success message
                console.log(jsonResponse);
                self.success = jsonResponse.success;
                self.errors = jsonResponse.errors;
            })
            .catch(function (error) {
                console.log(error);
            });


    });
    $(function () {
        $("#mdb-lightbox-ui").load("mdb-addons/mdb-lightbox-ui.html");
    });

    $('#inputGroupFile02').on('change', function () {
        //get the file name
        var fileName = $(this).val();
        //replace the "Choose a file" label
        $(this).next('.custom-file-label').html(fileName);
    })
        
});