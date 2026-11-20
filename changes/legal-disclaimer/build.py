# Builds Privacy Policy / Legal Disclaimer pages (EN + ES) and the contact-form notice.
# DRAFT text: must be reviewed by the client (and Spanish reviewer) before launch.
import re,html,os
ADDR_EN="2625 Redwing Road, Suite 205, Fort Collins, Colorado 80526"
def blk(items):
    o=[]
    for k,v in items:
        if k=='h2': o.append(f'<!-- wp:heading -->\n<h2 class="wp-block-heading">{v}</h2>\n<!-- /wp:heading -->')
        elif k=='p': o.append(f'<!-- wp:paragraph -->\n<p>{v}</p>\n<!-- /wp:paragraph -->')
        elif k=='ul':
            li=''.join(f'<!-- wp:list-item -->\n<li>{x}</li>\n<!-- /wp:list-item -->\n' for x in v)
            o.append(f'<!-- wp:list -->\n<ul class="wp-block-list">\n{li}</ul>\n<!-- /wp:list -->')
    return '\n\n'.join(o)+'\n'
EN=[
('p','<em>Last updated: November 2026. This is a draft pending client approval.</em>'),
('h2','Who We Are'),
('p',f'This website is operated by Elevated Family Law, LLC ("we," "us," or "our"), a family law practice located at {ADDR_EN}. You can reach us at <a href="tel:+19707974757">(970) 797-4757</a> or <a href="mailto:info@elevatedfamilylaw.com">info@elevatedfamilylaw.com</a>.'),
('h2','Information We Collect'),
('ul',['<strong>Information you give us.</strong> If you use our consultation request form, we receive the information you enter: your name, phone number, email address, county or jurisdiction, preferred contact times and days, the type of consultation, and your description of your matter.',
 '<strong>Information collected automatically.</strong> When you visit the site, our analytics tools may collect your IP address, browser and device type, the pages you view, how you arrived at the site, and how long you stay.']),
('h2','How We Use Your Information'),
('ul',['To respond to your consultation request and contact you about your matter.','To operate, secure, and improve this website.','To understand how visitors use the site, using aggregated analytics.','To comply with legal and professional obligations.']),
('h2','Contact Form and Service Providers'),
('p','Our consultation form is processed by Web3Forms, a third-party form service that delivers your submission to our email. We use other service providers to run this website, including website hosting (Amazon Web Services), Google Analytics, Jetpack (Automattic) site statistics, and Google Fonts. These providers may process information such as your IP address and browsing activity under their own privacy policies.'),
('p','<strong>We do not sell your personal information.</strong> We share it only with service providers that help us operate the site and our practice, when required by law, or with your permission.'),
('h2','Cookies and Analytics'),
('p','This website uses cookies and similar technologies for the following purposes: remembering your language choice (English or Spanish), and measuring site traffic through Google Analytics and Jetpack. You can block or delete cookies in your browser settings, and you can opt out of Google Analytics using the <a href="https://tools.google.com/dlpage/gaoptout">Google Analytics opt-out browser add-on</a>. Blocking cookies will not prevent you from using the site.'),
('h2','How Long We Keep Information'),
('p','We keep consultation requests for as long as needed to respond and to meet our legal and professional record-keeping obligations. If you become a client, your information is handled under our engagement agreement and the professional rules that apply to attorneys. Analytics data is kept according to the settings of each analytics provider.'),
('h2','Your Choices'),
('p','You may ask us to correct or delete information you sent through this website, or ask what we hold about you, by contacting us at the email address above. We will respond as required by law. We may need to keep some information for legal or professional reasons.'),
('h2','Security'),
('p','We take reasonable steps to protect information sent through this website, including secure (HTTPS) connections. No method of transmission over the internet is completely secure, so please do not send sensitive or confidential information through the contact form (see the Legal Disclaimer below).'),
('h2','Children'),
('p','This website is not directed to children under 13, and we do not knowingly collect personal information from children.'),
('h2','Changes to This Policy'),
('p','We may update this policy from time to time. The "Last updated" date at the top shows when it was last changed.'),
('h2','Legal Disclaimer'),
('p','<strong>General information only.</strong> The content of this website is provided for general informational purposes. It is not legal advice and should not be relied on as legal advice for your situation. Laws change, and the information may not apply to your circumstances or outside Colorado.'),
('p','<strong>No attorney-client relationship.</strong> Visiting this website, reading its content, or sending us a message or form submission does not create an attorney-client relationship. A relationship is created only when we agree in writing to represent you.'),
('p','<strong>Do not send confidential information.</strong> Messages sent through this website or by email may not be confidential or privileged. Please do not include sensitive details about your case until we have agreed to represent you.'),
('p','<strong>Testimonials and results.</strong> Testimonials reflect the individual experiences of the people quoted. Every case is different, and past results do not guarantee a similar outcome in your matter.'),
('p','<strong>Attorney advertising.</strong> This website may be considered attorney advertising under the Colorado Rules of Professional Conduct.'),
('p',f'<strong>Contact.</strong> Elevated Family Law, LLC, {ADDR_EN}. Phone <a href="tel:+19707974757">(970) 797-4757</a>. Email <a href="mailto:info@elevatedfamilylaw.com">info@elevatedfamilylaw.com</a>.'),
]
ES=[
('p','<em>Última actualización: noviembre de 2026. Este es un borrador pendiente de aprobación del cliente.</em>'),
('h2','Quiénes Somos'),
('p',f'Este sitio web es operado por Elevated Family Law, LLC («nosotros» o «nuestro»), un bufete de derecho familiar ubicado en {ADDR_EN}. Puede comunicarse con nosotros al <a href="tel:+19707974757">(970) 797-4757</a> o en <a href="mailto:info@elevatedfamilylaw.com">info@elevatedfamilylaw.com</a>.'),
('h2','Información que Recopilamos'),
('ul',['<strong>Información que usted nos proporciona.</strong> Si utiliza nuestro formulario de solicitud de consulta, recibimos la información que usted ingresa: su nombre, número de teléfono, correo electrónico, condado o jurisdicción, horarios y días preferidos de contacto, el tipo de consulta y la descripción de su asunto.',
 '<strong>Información recopilada automáticamente.</strong> Cuando visita el sitio, nuestras herramientas de análisis pueden recopilar su dirección IP, el tipo de navegador y dispositivo, las páginas que consulta, cómo llegó al sitio y cuánto tiempo permanece en él.']),
('h2','Cómo Usamos Su Información'),
('ul',['Para responder a su solicitud de consulta y comunicarnos con usted sobre su asunto.','Para operar, proteger y mejorar este sitio web.','Para entender cómo los visitantes usan el sitio, mediante análisis agregados.','Para cumplir con obligaciones legales y profesionales.']),
('h2','Formulario de Contacto y Proveedores de Servicios'),
('p','Nuestro formulario de consulta es procesado por Web3Forms, un servicio externo de formularios que entrega su envío a nuestro correo electrónico. Utilizamos otros proveedores de servicios para operar este sitio web, incluyendo el alojamiento web (Amazon Web Services), Google Analytics, las estadísticas de Jetpack (Automattic) y Google Fonts. Estos proveedores pueden procesar información como su dirección IP y su actividad de navegación conforme a sus propias políticas de privacidad.'),
('p','<strong>No vendemos su información personal.</strong> Solo la compartimos con proveedores de servicios que nos ayudan a operar el sitio y nuestra práctica, cuando la ley lo exige o con su permiso.'),
('h2','Cookies y Análisis'),
('p','Este sitio web usa cookies y tecnologías similares para lo siguiente: recordar su elección de idioma (inglés o español) y medir el tráfico del sitio mediante Google Analytics y Jetpack. Puede bloquear o eliminar las cookies en la configuración de su navegador, y puede optar por no participar en Google Analytics con el <a href="https://tools.google.com/dlpage/gaoptout">complemento de exclusión de Google Analytics</a>. Bloquear las cookies no le impedirá usar el sitio.'),
('h2','Por Cuánto Tiempo Conservamos la Información'),
('p','Conservamos las solicitudes de consulta durante el tiempo necesario para responder y cumplir con nuestras obligaciones legales y profesionales de conservación de registros. Si usted se convierte en cliente, su información se maneja conforme a nuestro acuerdo de representación y a las normas profesionales aplicables a los abogados. Los datos de análisis se conservan según la configuración de cada proveedor.'),
('h2','Sus Opciones'),
('p','Puede solicitarnos que corrijamos o eliminemos la información que envió a través de este sitio web, o preguntarnos qué información tenemos sobre usted, comunicándose con nosotros al correo electrónico indicado arriba. Responderemos según lo exija la ley. Es posible que debamos conservar cierta información por razones legales o profesionales.'),
('h2','Seguridad'),
('p','Tomamos medidas razonables para proteger la información enviada a través de este sitio web, incluyendo conexiones seguras (HTTPS). Ningún método de transmisión por internet es completamente seguro, por lo que le pedimos que no envíe información delicada o confidencial a través del formulario de contacto (consulte el Aviso Legal más abajo).'),
('h2','Menores de Edad'),
('p','Este sitio web no está dirigido a menores de 13 años y no recopilamos intencionalmente información personal de menores.'),
('h2','Cambios a Esta Política'),
('p','Podemos actualizar esta política de vez en cuando. La fecha de «Última actualización» al inicio indica cuándo se modificó por última vez.'),
('h2','Aviso Legal'),
('p','<strong>Solo información general.</strong> El contenido de este sitio web se ofrece con fines informativos generales. No constituye asesoría legal y no debe utilizarse como tal para su situación. Las leyes cambian y la información puede no aplicarse a sus circunstancias ni fuera de Colorado.'),
('p','<strong>No se crea una relación abogado-cliente.</strong> Visitar este sitio web, leer su contenido o enviarnos un mensaje o formulario no crea una relación abogado-cliente. Esa relación solo se establece cuando aceptamos representarle por escrito.'),
('p','<strong>No envíe información confidencial.</strong> Los mensajes enviados a través de este sitio web o por correo electrónico pueden no ser confidenciales ni estar protegidos por el secreto profesional. Le pedimos que no incluya detalles delicados sobre su caso hasta que hayamos aceptado representarle.'),
('p','<strong>Testimonios y resultados.</strong> Los testimonios reflejan las experiencias individuales de las personas citadas. Cada caso es diferente, y los resultados pasados no garantizan un resultado similar en su asunto.'),
('p','<strong>Publicidad de abogados.</strong> Este sitio web puede considerarse publicidad de abogados conforme a las Reglas de Conducta Profesional de Colorado.'),
('p',f'<strong>Contacto.</strong> Elevated Family Law, LLC, {ADDR_EN}. Teléfono <a href="tel:+19707974757">(970) 797-4757</a>. Correo electrónico <a href="mailto:info@elevatedfamilylaw.com">info@elevatedfamilylaw.com</a>.'),
]
os.makedirs('new',exist_ok=True)
open('new/privacy_en.html','w').write(blk(EN))
open('new/privacy_es.html','w').write(blk(ES))
# contact form notice (inserted above the Submit button)
NOTE={'en':'Submitting this form does not create an attorney-client relationship. Please do not include confidential or sensitive details until we have agreed to represent you. See our <a href="{pp}">Privacy Policy</a>.',
      'es':'Enviar este formulario no crea una relación abogado-cliente. Le pedimos que no incluya detalles confidenciales o delicados hasta que hayamos aceptado representarle. Consulte nuestra <a href="{pp}">Política de Privacidad</a>.'}
PP={'en':'/privacy-policy/','es':'/es/politica-de-privacidad/'}
for lang,pid in (('en',15),('es',168)):
    src=f'backup-original/{pid}.html'
    s=open(src).read()
    a='<button type="submit" class="efl-submit">'
    assert s.count(a)==1
    note=f'<p class="efl-form-note" style="font-size:0.85rem;color:#4d5a5a;margin:0 0 1rem;">{NOTE[lang].format(pp=PP[lang])}</p>\n    '
    open(f'new/contact_{pid}.html','w').write(s.replace(a,note+a))
print('ok')
