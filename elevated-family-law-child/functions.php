<?php
/**
 * Elevated Family Law child theme functions.
 */

add_action( 'wp_enqueue_scripts', function () {
    $parent_style = 'twentyseventeen-style';
    wp_enqueue_style( $parent_style, get_template_directory_uri() . '/style.css', array(), '2026.11.11' );
    wp_enqueue_style( 'elevated-family-law-style', get_stylesheet_uri(), array( $parent_style ), '2026.11.11' );
} );
