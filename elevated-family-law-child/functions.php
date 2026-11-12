<?php
/**
 * Elevated Family Law child theme functions.
 */

add_action( 'wp_enqueue_scripts', function () {
    $parent_style = 'twentyseventeen-style';
    $version      = wp_get_theme()->get( 'Version' );
    wp_enqueue_style( $parent_style, get_template_directory_uri() . '/style.css', array(), $version );
    wp_enqueue_style( 'elevated-family-law-style', get_stylesheet_uri(), array( $parent_style ), $version );
} );
