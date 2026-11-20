<?php
/**
 * Displays header media
 *
 * Child theme override: adds the custom logo at the top-left of the header.
 *
 * @package WordPress
 * @subpackage Twenty_Seventeen
 * @since Twenty Seventeen 1.0
 * @version 1.0
 */

?>
<div class="custom-header">

		<div class="custom-header-media">
			<?php the_custom_header_markup(); ?>
		</div>

	<?php if ( function_exists( 'the_custom_logo' ) && has_custom_logo() ) : ?>
		<div class="efl-header-logo">
			<?php the_custom_logo(); ?>
		</div>
	<?php endif; ?>

	<?php get_template_part( 'template-parts/header/site', 'branding' ); ?>

</div><!-- .custom-header -->
