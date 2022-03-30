cod_entidade = '465'
selects = {
'TipoServico' : """select
                    distinct
                    coalesce(v.cor, 'INDEFINIDA') ||'|' as extractCor
                    from
                    bethadba.veiculos v """,

}