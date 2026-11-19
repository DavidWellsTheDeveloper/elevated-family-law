import re,html
# Builds the visual version of each service page from backup-original/<id>.html
# Spec: key fact, sections [(heading|None(existing)|block idx, [block idxs], pullquote_block_idx)], intro, closing
SPEC={ # en_id: dict
110:dict(es=174,intro=[0],secs=[(1,[2],None),(3,[4],4),(5,[6],None),(7,[8,9],None)],close=[10,11]),
117:dict(es=175,intro=[0,1,2],secs=[(3,[4],None),(5,[6,7],None),(8,[9,10,11],10)],close=[12]),
122:dict(es=176,intro=[0,1],secs=[('H0',[2,3],None),('H1',[4,5],4),('H2',[6,7,8],None)],close=[9]),
128:dict(es=177,intro=[],secs=[('H0',[0,1,2],None),('H1',[3,4],4),('H2',[5,6,7],None)],close=[8,9]),
132:dict(es=178,intro=[],secs=[(0,[1],None),('H0',[2],2),('H1',[3,4],None),('H2',[5,6],None)],close=[7,8]),
}
TXT={
'en':{110:dict(kf="In Colorado, divorce is called a Dissolution of Marriage. Most cases reach a settlement before trial.",pq="A governing principle of this process is the full disclosure of all relevant financial information to the other party.",H=[]),
117:dict(kf="An APR case lets parents who were never married ask the Court for a parenting schedule, decision-making authority, and child support.",pq="While such a report and recommendations is helpful to the Court, it is not binding upon the Court.",H=[]),
122:dict(kf="Planning to move with your children? Colorado law requires a specific legal process, and the standard the Court applies depends on whether parenting orders already exist.",pq="A minority time parent cannot Petition to relocate with minor child.",H=["Two Legal Standards","Who Can Petition to Relocate","A Two-Step Process"]),
128:dict(kf="Most family law cases settle before a final trial, and settling often gives you more control over the outcome.",pq="In fact, statistics show the majority of cases are settled before ever reaching a final trial.",H=["Alternatives to Trial","Why Settlement Matters","Keeping Control of Your Outcome"]),
132:dict(kf="Filing an Emergency Motion to Restrict Parenting Time makes parenting time supervised right away, with a hearing set within 14 days.",pq="Imminent danger is not about harm from six months or a year ago. It must be a danger that is sure to occur right now.",H=["What Counts as Imminent Danger","What Happens After Filing","Protecting Yourself From False Claims"])},
'es':{110:dict(kf="En Colorado, el divorcio se llama Disolución del Matrimonio. La mayoría de los casos llegan a un acuerdo antes del juicio.",pq="Un principio rector de este proceso es la divulgación completa de toda la información financiera relevante a la otra parte.",H=[]),
117:dict(kf="Un caso de APR permite que los padres que nunca se casaron soliciten al Tribunal un horario de crianza, autoridad para la toma de decisiones y manutención de menores.",pq="Aunque este informe y sus recomendaciones son útiles para el Tribunal, no son vinculantes.",H=[]),
122:dict(kf="¿Planea mudarse con sus hijos? La ley de Colorado exige un proceso legal específico, y el criterio que aplica el Tribunal depende de si ya existen órdenes de crianza.",pq="El padre o la madre con la minoría del tiempo no puede solicitar la reubicación con un menor.",H=["Dos Criterios Legales","Quién Puede Solicitar la Reubicación","Un Proceso de Dos Pasos"]),
128:dict(kf="La mayoría de los casos de derecho familiar se resuelven antes de un juicio final, y llegar a un acuerdo a menudo le da más control sobre el resultado.",pq="De hecho, las estadísticas muestran que la mayoría de los casos se resuelven antes de llegar a un juicio final.",H=["Alternativas al Juicio","Por Qué Importa Llegar a un Acuerdo","Mantenga el Control del Resultado"]),
132:dict(kf="Presentar una Moción de Emergencia para Restringir el Tiempo de Crianza hace que el tiempo de crianza sea supervisado de inmediato, con una audiencia dentro de 14 días.",pq="El peligro inminente no se refiere a un daño ocurrido hace seis meses o hace un año. Debe ser un peligro que ocurrirá con seguridad en este momento.",H=["Qué se Considera Peligro Inminente","Qué Ocurre Después de Presentar la Moción","Cómo Protegerse de Acusaciones Falsas"])}}
def blocks(s): return [m.group(0) for m in re.finditer(r'<!-- wp:(\w+)[^>]*-->.*?<!-- /wp:\1 -->',s,re.S)]
def h2(t): return f'<!-- wp:heading -->\n<h2 class="wp-block-heading">{t}</h2>\n<!-- /wp:heading -->'
def inner(b): return re.search(r'<(?:p|h2)[^>]*>(.*?)</(?:p|h2)>',b,re.S).group(1)
def build(src,lang,eid):
    B=blocks(open(src).read()); sp=SPEC[eid]; t=TXT[lang][eid]
    assert len(B)>=10
    out=[]
    out.append(f'<!-- wp:group {{"className":"efl-keyfact"}} -->\n<div class="wp-block-group efl-keyfact"><!-- wp:paragraph -->\n<p>{t["kf"]}</p>\n<!-- /wp:paragraph --></div>\n<!-- /wp:group -->')
    out+= [B[i] for i in sp['intro']]
    for n,(head,idxs,pq) in enumerate(sp['secs']):
        side='efl-left' if n%2==0 else 'efl-right'
        if isinstance(head,str): hb=h2(t['H'][int(head[1])])
        else: hb=B[head] if 'heading' in B[head][:20] else h2(inner(B[head]))
        parts=[hb]
        for i in idxs:
            parts.append(B[i])
            if pq==i: parts.append(f'<!-- wp:pullquote {{"className":"efl-pullquote"}} -->\n<figure class="wp-block-pullquote efl-pullquote"><blockquote><p>{t["pq"]}</p></blockquote></figure>\n<!-- /wp:pullquote -->')
        out.append(f'<!-- wp:group {{"className":"efl-section-card {side}"}} -->\n<div class="wp-block-group efl-section-card {side}">'+'\n\n'.join(parts)+'</div>\n<!-- /wp:group -->')
    out+= [B[i] for i in sp['close']]
    return '\n\n'.join(out)+'\n'
import os
os.makedirs('new',exist_ok=True)
for eid,sp in SPEC.items():
    open(f'new/{eid}.html','w').write(build(f'backup-original/{eid}.html','en',eid))
    open(f'new/{sp["es"]}.html','w').write(build(f'backup-original/{sp["es"]}.html','es',eid))
print('ok')
