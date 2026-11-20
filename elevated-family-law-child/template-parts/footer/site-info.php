<?php
/**
 * Displays footer site info
 *
 * Child theme override: privacy link (language aware), imprint link, and a
 * small attorney advertising / legal disclaimer in English or Spanish.
 *
 * @package WordPress
 * @subpackage Twenty_Seventeen
 * @since Twenty Seventeen 1.0
 * @version 1.0
 */

$efl_is_es = function_exists( 'pll_current_language' ) && 'es' === pll_current_language();

$efl_pp_id = (int) get_option( 'wp_page_for_privacy_policy' );
if ( $efl_pp_id && function_exists( 'pll_get_post' ) ) {
	$efl_pp_translated = pll_get_post( $efl_pp_id );
	if ( $efl_pp_translated ) {
		$efl_pp_id = (int) $efl_pp_translated;
	}
}

if ( $efl_is_es ) {
	$efl_disclaimer = 'La información de este sitio web es solo de carácter informativo general y no constituye asesoría legal. Visitar este sitio o comunicarse con nosotros a través de él no crea una relación abogado-cliente. Los testimonios reflejan experiencias individuales; los resultados pasados no garantizan un resultado similar. Este sitio web puede considerarse publicidad de abogados.';
	$efl_disclaimer_link = 'Política de Privacidad y Aviso Legal';
} else {
	$efl_disclaimer = 'The information on this website is for general informational purposes only and is not legal advice. Visiting this site or contacting us through it does not create an attorney-client relationship. Testimonials reflect individual experiences; past results do not guarantee a similar outcome. This website may be considered attorney advertising.';
	$efl_disclaimer_link = 'Privacy Policy &amp; Legal Disclaimer';
}
?>
<div class="site-info">
	<?php if ( $efl_pp_id && 'publish' === get_post_status( $efl_pp_id ) ) : ?>
		<a href="<?php echo esc_url( get_permalink( $efl_pp_id ) ); ?>" class="privacy-policy-link"><?php echo esc_html( get_the_title( $efl_pp_id ) ); ?></a><span role="separator" aria-hidden="true"></span>
	<?php endif; ?>
	<a href="<?php echo esc_url( 'https://focowebsites.com/' ); ?>" class="imprint">
		<?php esc_html_e( 'Built by FoCo Websites', 'twentyseventeen' ); ?>
	</a>
</div><!-- .site-info -->
<div class="efl-footer-disclaimer">
	<p>
		<?php echo esc_html( $efl_disclaimer ); ?>
		<?php if ( $efl_pp_id && 'publish' === get_post_status( $efl_pp_id ) ) : ?>
			<a href="<?php echo esc_url( get_permalink( $efl_pp_id ) ); ?>"><?php echo wp_kses_post( $efl_disclaimer_link ); ?></a>.
		<?php endif; ?>
		<br>Elevated Family Law, LLC &middot; 2625 Redwing Road, Suite 205, Fort Collins, Colorado 80526
	</p>
</div><!-- .efl-footer-disclaimer -->
