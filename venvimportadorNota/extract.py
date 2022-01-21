ServicoAeItem = """select 
430 ||'|'||
si.servcatcod ||'|'||
si.servcatdesc ||'|' as extractServicoAeItem
from arr_servcat si""" 

ServicoAeSubItem = """select 
430 ||'|'||
substring(ssi.servitemcodmun from 4 for 5) ||'|'||
ssi.servitemdesc ||'|'||
ssi.servcatcod ||'|'||
replace(cast(ssi.servitemaliqiss as varchar), '.', ',') ||'|' as extractServicoSubItem 
from arr_servitem ssi
order by servcatcod, servitemcodmun"""

Pessoa = """--Pessoa Equiplano
--76030717000148|2|0|Equiplano Sistemas||||82510350|Rua Ernesto Piazetta|202|Empresa|Bacacheri|Curitiba|||Equiplano Sistemas|2||0|2|
select
430 ||'|'||
translate (p.concpfcnpj, '.-/','') ||'|'||
p.connat ||'|'||
case ce.bcesituacao 
	when 1 then 2
	when 2 then 3
Else '0'
end  ||'|'||
regexp_replace(translate(substring(initcap(coalesce(p.connom, '')) from 1 for 80), '|', ''),E'[

]+','') ||'|'||
coalesce (cast(ce.bcecod as varchar), '') ||'|'||
p.coninsest ||'|'||
initcap(p.confan) ||'|'||
p.concep ||'|'||
regexp_replace(initcap(substring(p.conend from 1 for 40)),E'[

]+','') ||'|'||
p.connum ||'|'||
initcap(substring(p.concom from 1 for 40)) ||'|'||
initcap(p.conbai )||'|'||
initcap(c.munnom) ||'|'||
case p.confone
	when '' then p.confonecel 
	else '' end ||'|'|| 
regexp_replace(p.conemail,E'[

]+','') ||'|'||
regexp_replace(initcap(substring(p.concom from 1 for 40)),E'[

]+','') ||'|'||
case ce.bcesimpnac 
	when 1 then 1
	when 2 then 2
	Else '2' end ||'|'||
regexp_replace(p.conemail,E'[

]+','') ||'|'||
case ce.bceisstip
	when 1 then 1
	when 2 then 3
	when 3 then 2
	when 4 then 4
	Else 0
end ||'|'||
case ce.bceregesptrib
	when 5 then 1
Else 2 end ||'|'||
c.muncod ||'|' as ExtractPessoa
from arr_con p
join arr_mun1 c on (c.muncod = p.conmuncod)
left join arr_bce ce on (ce.bceconcod = p.concod)
--where p.concpfcnpj = '22.013.233/0001-61'"""

Operador = """--Operador Equiplano
--430|Esmaster|76030717000148|227913479860275300272673954531763843008|76030717000148|Equiplano Sistemas|2|Conversao de Sistema.|
select
430 ||'|'||
regexp_replace(initcap(substring(c.connom from 1 for 20)),E'[

]+','') ||'|'||
translate(c.concpfcnpj, '.-/','') ||'|'||
'227913479860275300272673954531763843008' ||'|'||
translate(c.concpfcnpj, '.-/','') ||'|'||
regexp_replace(initcap(c.connom),E'[

]+','') ||'|'||
c.connat ||'|'||
'Conversao de Sistema.' ||'|'
from ARR_BCE e
left join arr_bceusuweb ue on (ue.bcecod = e.bcecod)
join arr_con c on (c.concod = e.bceconcod)
group by c.concpfcnpj, c.connom, c.connat
UNION
select
430 ||'|'||
regexp_replace(initcap(substring(u.usuwebnom from 1 for 20)),E'[

]+','') ||'|'||
translate(u.usuwebcpfcnpj, '.-/','') ||'|'||
'227913479860275300272673954531763843008' ||'|'||
translate(u.usuwebcpfcnpj, '.-/','') ||'|'||
regexp_replace(initcap(u.usuwebnom),E'[

]+','') ||'|'||
case 
	when length(u.usuwebcpfcnpj) > 14 then 2
	else 1 end ||'|'||
'Conversao de Sistema.' ||'|'
from arr_usuweb u""" 

PapelOperador = """select * from arr_con""" 

Nota = """select 
distinct(432, n."Número da nota fiscal", n."Número de verificação da nota fiscal"),
n."Data e hora da emissão" as DtEmissaoNfs,
case pn."Tipo da pessoa"
	when 'F' then '1'
	else 2 end as TpPessoaPrestador,
lpad(cast(n."CPF ou CNPJ do prestador" as varchar), 14,'0') as NrDocumentoPrestador,
n."Nome do prestador" as NmPessoaPrestador,
432 as identidadeTomador,
case tn."Tipo da pessoa"
	when 'F' then '1'
	when 'J' then '2'
	else '' end as tipoTomador,	
case tn."Tipo da pessoa"
	when 'F' then lpad(cast(tn."CPF ou CNPJ do tomador" as varchar), 11,'0')
	when 'J' then lpad(cast(tn."CPF ou CNPJ do tomador" as varchar), 14,'0')
	else '' end as NrDocumentoTomador,
coalesce(tn."Nome da pessoa", '') as NmPessoaTomador,
o."IdEntidade" as identidadeOperador,
o."NmOperadorPessoa" as NmOperadorPessoa, --até 20 caracteres
lpad(cast(o."NrDocumentoOperador" as varchar), 14,'0') as NrDocumentoOperador,
o."NmPessoaOperador" as NmPessoaOperador,
o."TpPessoaOperador" as TpPessoaOperador,
lpad(cast(o."NrDocumentoOperador" as varchar), 14,'0') as DsLogin,
translate(coalesce(cast(n."Valor da COFINS" as varchar), '0'), '.', ',') as VlCofins,
translate(coalesce(cast(n."Valor da CSLL" as varchar), '0'), '.', ',') as VlCsll,
translate(coalesce(cast(n."Valor do INSS" as varchar), '0'), '.', ',') as VlInss,
translate(coalesce(cast(n."Valor do Imposto de Renda" as varchar), '0'), '.', ',') as VlIrpj,
translate(coalesce(cast(n."Valor do PIS PASEP" as varchar), '0'), '.', ',') as VlPis,
n."Deduções" as VlTotalDeducoes,
translate(cast(n."valor do serviço" as varchar), '.', ',') as VlTotalNota,
'' as IdRps,
'' as IdNfsSubstituicao,
coalesce (n."Responsável pela retenção do ISS", '2' ) as IsIssRetido,
n."Natureza da operação" as TpTributacao,
translate(cast(n."Imposto gerado" as varchar), '.', ',') as VlImposto,
case n."Optante do simples"
	when 'S' then '1'
	else '2' end as TpOpcaoSimplesNfs,
translate(coalesce(cast(n."Alíquota COFINS" as varchar), '0'), '.', ',') as VlAliquotaCofins,
translate(coalesce(cast(n."Alíquota CSLL" as varchar), '0'), '.', ',') as VlAliquotaCsll,
translate(coalesce(cast(n."Alíquota do INSS" as varchar), '0'), '.', ',') as VlAliquotaInss,
translate(coalesce(cast(n."Alíquota do IR" as varchar), '0'), '.', ',') as VlAliquotaIrpj,
translate(coalesce(cast(n."Alíquota do PIS" as varchar), '0'), '.', ',') as VlAliquotaPis,
'432' as IdEntidadeVencimento,
n."Código da competência" as CompetenciaServico,
'2021' as ExercicioServico,
'1' as TpDocumentoFiscal,
'4120408' as CdIbge,
(select c."Código junto ao IBGE" from cidade c where c."Código do município" = (select ns."Código do município" 
 	from nota_servico ns 
 	where ns."Código da pessoa" = n."Código da pessoa" and ns."Número da nota fiscal" = n."Número da nota fiscal"
 	group by ns."Código da pessoa", ns."Número da nota fiscal", ns."Código do município")) as CdIbgeLocalTributacao,
translate(cast(n."Desconto incondicional" as varchar), '.', ',') as VlDesconto
from nota n
left join prestador_nota pn on (pn."Código da pessoa" = n."Código da pessoa" and pn."Número da nota fiscal" = n."Número da nota fiscal")
left join tomador_nota tn on (tn."Código do tomador" = n."Código do tomador" and tn."Número da nota fiscal" = n."Número da nota fiscal" and tn."Código da pessoa" = n."Código da pessoa")
left join operador o on (lpad(cast(o."NrDocumentoOperador" as varchar), 14,'0') = lpad(cast(n."CPF ou CNPJ do prestador" as varchar), 14,'0'))
order by n."Código da competência", n."Data e hora da emissão"


""" 

