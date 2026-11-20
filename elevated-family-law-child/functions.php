<?php
/**
 * Elevated Family Law child theme functions.
 */

/**
 * Enable the Customizer background color control (Appearance > Customize >
 * Colors > Background Color). The parent theme does not support it.
 * Default is white; the current site color is stored in the theme mod.
 */
add_action( 'after_setup_theme', function () {
    add_theme_support( 'custom-background', array(
        'default-color' => 'ffffff',
    ) );
} );

add_action( 'wp_enqueue_scripts', function () {
    $parent_style = 'twentyseventeen-style';
    $version      = wp_get_theme()->get( 'Version' );
    wp_enqueue_style( $parent_style, get_template_directory_uri() . '/style.css', array(), $version );
    wp_enqueue_style( 'elevated-family-law-style', get_stylesheet_uri(), array( $parent_style ), $version );

    // On the front page the parent theme keeps the header image fixed behind the
    // content, so the content wrapper must be opaque. Use the Customizer
    // background color (changes show after saving/publishing).
    $bg = get_background_color();
    if ( $bg ) {
        wp_add_inline_style(
            'elevated-family-law-style',
            '.twentyseventeen-front-page .site-content-contain { background-color: #' . esc_attr( $bg ) . '; }'
        );
    }
} );

/**
 * Keep the site out of search engines while it is on the development domain.
 *
 * TODO: Remove this block (or set EFL_BLOCK_INDEXING to false) when the site
 * moves to the permanent domain. See "Search Engine Indexing" in PRD.md.
 */
if ( ! defined( 'EFL_BLOCK_INDEXING' ) ) {
    define( 'EFL_BLOCK_INDEXING', true );
}

if ( EFL_BLOCK_INDEXING ) {
    // X-Robots-Tag HTTP header.
    add_action( 'send_headers', function () {
        header( 'X-Robots-Tag: noindex, nofollow', true );
    } );

    // <meta name="robots" content="noindex, nofollow"> in the page head.
    add_filter( 'wp_robots', function ( $robots ) {
        unset( $robots['index'], $robots['follow'], $robots['max-image-preview'] );
        $robots['noindex']  = true;
        $robots['nofollow'] = true;
        return $robots;
    }, 999 );
}
