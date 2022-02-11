cod_entidade = '324'
selects = {
'ParameterSystem' : "select ps.CODENTIDADE ||'|'|| ps.NMPARAMETERSYSTEM ||'|'|| ps.VLPARAMETERSYSTEM ||'|' as extractParameterSystem from Scf_ParameterSystem ps where codentidade = 324",
'Marca' : "select m.NMMARCA ||'|' as extractmarca from  MARCA m",
'Especie' : "select e.NMESPECIE ||'|'|| c.TPCATEGORIACNH ||'|'|| coalesce(e.TPESPECIEACUMULADOR, '') ||'|'|| coalesce(e.TPVEICULOTCE, '') ||'|'|| coalesce(e.TPNATUREZABENS, '') ||'|' as extractEspecie from  SCF_ESPECIE e join scf_CategoriaCnh c on (c.IDCATEGORIACNH = e.IDCATEGORIACNH)",
'Modelo' : f""" select
                  mo.NMMODELO ||'|'||
                  ma.NMMARCA ||'|'||
                  e.NMESPECIE ||'|'||
                  coalesce(mo.TPCOMBUSTIVELTCE, '') ||'|' as etractespecie 
                from 
                  scf_modelo mo
                    join MARCA ma on (ma.IDMARCA = mo.IDMARCA)
                    join SCF_ESPECIE e on (e.IDESPECIE = mo.IDESPECIE) """,
'TipoServico' : """select
                      ts.NMTIPOSERVICO ||'|'||
                      ts.TPAGENDAMENTOSERVICO ||'|' as extractTipoServico
                    from 
                      scf_TipoServico ts """,
'Motorista' : f""" select 
                    m.CODENTIDADE ||'|'||
                    m.NRCODIGOMOTORISTA ||'|'||
                    s.MATRICULA ||'|'||
                    coalesce(m.CODPESSOAFISICA, '') ||'|'||
                    m.NRREGISTROCNH ||'|'||
                    m.TPMODELOCNH ||'|'||
                    EXTRACT(day FROM m.DTPRIMEIRACNH) ||'/'|| EXTRACT(month FROM m.DTPRIMEIRACNH) ||'/'|| EXTRACT(year FROM m.DTPRIMEIRACNH) ||'|'||
                    EXTRACT(day FROM m.DTVALIDADECNH) ||'/'|| EXTRACT(month FROM m.DTVALIDADECNH) ||'/'|| EXTRACT(year FROM m.DTVALIDADECNH) ||'|'||
                    EXTRACT(day FROM m.DTEMISSAOCNH) ||'/'|| EXTRACT(month FROM m.DTEMISSAOCNH) ||'/'|| EXTRACT(year FROM m.DTEMISSAOCNH) ||'|' as ExtarctMotorista
                    from scf_motorista m 
                    left join servidor s on (s.idservidor=m.IDSERVIDOR) 
                    where 
                    m.codentidade={cod_entidade} """,
'Veiculo' : f""" select
                v.CODENTIDADE ||'|'||
                v.NRFROTA ||'|'||
                b.CODBEM ||'|'||
                v.NRPLACA ||'|'||
                e.NMESPECIE ||'|'||
                m.NMMODELO ||'|'||
                c.nmcor ||'|'||
                v.NRRENAVAM ||'|'||
                v.NRCHASSI ||'|'||
                v.NRMOTOR ||'|'||
                v.NRANOFABRICACAO ||'|'||
                v.NRANOMODELO ||'|'||
                v.NRPASSAGEIRO ||'|'||
                v.DSOBSERVACAO ||'|'||
                v.ISACUMULADORFUNCIONANDO ||'|'||
                v.TPVINCULO ||'|'||
                v.TPCOMBUSTIVEL ||'|'||
                EXTRACT(day FROM v.DTINCLUSAOSIMAM) ||'/'|| EXTRACT(month FROM v.DTINCLUSAOSIMAM) ||'/'|| EXTRACT(year FROM v.DTINCLUSAOSIMAM) ||'|'||
                replace(v.NRCILINDRADAS, '.',',') ||'|'||
                replace(v.NRPOTENCIAMOTOR, '.',',') ||'|'||
                replace(v.NRCAPACIDADETANQUECOMB, '.',',') ||'|'||
                replace(v.NRCAPACIDADECARGA, '.',',') ||'|'||
                v.IMPRESSAODIARIOBORDO ||'|'||
                coalesce(v.MEDIACONSUMO, '') ||'|' as extractMotorista 
                from 
                scf_veiculo v 
                    join scf_modelo m on (m.idmodelo = v.idmodelo) 
                    join scf_especie e on (e.idespecie = m.idespecie) 
                    join cor c on (c.idcor = v.idcor) 
                    left join bemobrigacao bo on (bo.idbemobrigacao = v.idbemobrigacao) 
                    left join scp55_bem b on (b.idbem = v.idbem) 
                where 
                v.codentidade={cod_entidade} """,
'Produto' : f""" select 
            p2.NOME ||'|'||
            p.CODPRODUTO ||'|'||
            p.TPPRODUTO ||'|'||
            coalesce(p.CODFABRICANTE, '') ||'|'||
            coalesce(p.DSOBSERVACAO, '') ||'|'||
            p.ISATIVO ||'|' as extractProduto
            from 
            produto p2
            join SCF_PRODUTO p on (p.codproduto = p2.CODPRODUTO) """,
'VeiculoProduto': f""" select 
                v.codentidade ||'|'|| 
                v.nrfrota ||'|'||
                p.codproduto ||'|'||
                p2.NOME ||'|' as extractVeiculoProduto
                from 
                scf_veiculoproduto vp 
                join scf_veiculo v on (v.idveiculo = vp.idveiculo) 
                join scf_produto p on (p.idproduto = vp.idproduto)
                join produto p2 on (p2.CODPRODUTO = p.CODPRODUTO) 
                where 
                v.codentidade={cod_entidade} """,
'CategoriaCnh' : f""" select 
                m.codentidade ||'|'|| 
                m.nrcodigomotorista ||'|'|| 
                cc.tpcategoriacnh ||'|' as extractMotoristaCatCnh
                from 
                scf_motoristacatcnh mc 
                join scf_motorista m on (m.idmotorista = mc.idmotorista) 
                join scf_categoriacnh cc on (cc.idcategoriacnh = mc.idcategoriacnh) 
                where 
                m.codentidade={cod_entidade} """,
'SituacaoCnh' : f""" select 
                m.codentidade ||'|'|| 
                m.nrcodigomotorista ||'|'||
                EXTRACT(day FROM ms.DTSITUACAOCNH) ||'/'|| EXTRACT(month FROM ms.DTSITUACAOCNH) ||'/'|| EXTRACT(year FROM ms.DTSITUACAOCNH) ||'|'||
                ms.IDSITUACAOCNH ||'|'||
                ms.NRPONTOSVIGENTES ||'|' as extractMotoristaSituacaoCnh
                from 
                scf_motoristasituacaocnh ms 
                join scf_motorista m on (m.idmotorista = ms.idmotorista) 
                where 
                m.codentidade={cod_entidade} """,
'VeiculoAbastecimento' : f""" select 
                        v.codentidade ||'|'||
                        va.NRABASTECIMENTO ||'|'||
                        v.nrfrota ||'|'||
                        b.codbem ||'|'||
                        p.codproduto ||'|'||
                        p2.NOME ||'|'||
                        m.NRCODIGOMOTORISTA ||'|'||
                        replace(va.VLUNITARIO, '.',',') ||'|'||
                        LPAD( EXTRACT( day FROM va.DTABASTECIMENTO ), 2, '0' ) ||'/'|| LPAD( EXTRACT( month FROM va.DTABASTECIMENTO ), 2, '0' ) ||'/'|| LPAD( EXTRACT( YEAR FROM va.DTABASTECIMENTO ), 4, '0' ) ||' '|| LPAD( EXTRACT( hour FROM va.DTABASTECIMENTO ), 2, '0' ) ||':'|| LPAD( EXTRACT( minute FROM va.DTABASTECIMENTO ), 2, '0' ) ||':'|| replace(LPAD( EXTRACT( second FROM va.DTABASTECIMENTO ), 2, '0' ), '.', '0') ||'|'||
                        replace(va.NRLITROSABASTECIMENTO, '.',',') ||'|'||
                        replace(va.VLABASTECIMENTO, '.',',') ||'|'||
                        va.TPABASTECIMENTO ||'|'|| 
                        coalesce(va.NRNOTAFISCAL,'') ||'|'||
                        va.DSOBSERVACAO ||'|'||
                        va.CODFORNECEDOR ||'|'||
                        coalesce(va.CODPESSOA,'') ||'|'||
                        coalesce(va.CODLOCAL,'') ||'|'||
                        coalesce(va.NRINTERNO,'') ||'|'||
                        va.ISACUMULADORFUNCIONANDO ||'|'||
                        coalesce(l.CODENTIDADE,'') ||'|'||
                        coalesce(l.EXERCICIO,'') ||'|'||
                        coalesce(l.NUMEROLIQUIDACAO,'') ||'|'||
                        coalesce(l.EXERCICIOLIQUIDACAO,'') ||'|'||
                        coalesce(l.CODENTIDADEORIGEM,'') ||'|'||
                        coalesce(e.CODENTIDADE,'') ||'|'||
                        coalesce(e.EXERCICIO,'') ||'|'||
                        coalesce(e.NUMEROEMPENHO,'') ||'|'||
                        coalesce(e.EXERCICIOEMPENHO,'') ||'|'||
                        coalesce(e.CODENTIDADEORIGEM,'') ||'|' as extractVeiculoAbastecimento
                        from 
                        scf_veiculoabastecimento va 
                        join scf_veiculo v on (v.idveiculo = va.idveiculo)
                        join SCF_MOTORISTA m on (m.IDMOTORISTA = va.IDMOTORISTA) 
                        left join scp55_bem b on (b.idbem=v.idbem) 
                        left join scf_produto p on (p.idproduto = va.idproduto) 
                        left join produto p2 on (p2.CODPRODUTO = p.CODPRODUTO)
                        left join SCP55_LIQUIDACAO l on (l.IDLIQUIDACAO = va.IDLIQUIDACAO)
                        left join SCP55_EMPENHO e on (e.IDEMPENHO = va.IDEMPENHO)
                        where 
                        v.codentidade={cod_entidade} """,
'Acumulador' : f""" select 
                v.CODENTIDADE ||'|'||
                v.nrfrota ||'|'||
                b.codbem ||'|'||
                LPAD( EXTRACT( day FROM va.DTLEITURAACUMULADOR), 2, '0' ) ||'/'|| LPAD( EXTRACT( month FROM va.DTLEITURAACUMULADOR), 2, '0' ) ||'/'|| LPAD( EXTRACT( YEAR FROM va.DTLEITURAACUMULADOR), 4, '0' ) ||' '|| LPAD( EXTRACT( hour FROM va.DTLEITURAACUMULADOR), 2, '0' ) ||':'|| LPAD( EXTRACT( minute FROM va.DTLEITURAACUMULADOR), 2, '0' ) ||':'|| replace(LPAD( EXTRACT( second FROM va.DTLEITURAACUMULADOR), 2, '0' ), '.', '0') ||'|'||
                va.TPORIGEMLEITURAACUMULADOR ||'|'||
                coalesce(vab.nrabastecimento, '') ||'|'||
                replace(va.VLACUMULADOR, '.', ',') ||'|'||
                coalesce(va.TMPVLACUMULADOR, '') ||'|' as ExtractAcumulador
                from 
                scf_veiculoacumulador va 
                join scf_veiculo v on (v.idveiculo = va.idveiculo) 
                join scp55_bem b on (b.idbem = v.idbem) 
                left join scf_veiculoabastecimento vab on (vab.idveiculoabastecimento = va.idveiculoabastecimento) 
                where 
                v.codentidade={cod_entidade} """,
'ConsumoCombustivel' : f"""select 
                    v.codentidade ||'|'|| 
                    cc.nrsequencial ||'|'|| 
                    v.nrfrota ||'|'|| 
                    cc.NRMES ||'|'|| 
                    cc.NRANO ||'|'|| 
                    cc.IDTIPOCATEGORIAOBJETODESPESA ||'|'|| 
                    cc.IDTIPOOBJETODESPESA ||'|'|| 
                    replace(cc.NRQUANTIDADE, '.', ',') ||'|' as extractConsumoCombustive
                    from 
                    scf_consumocombustivel cc 
                    join scf_veiculo v on (v.idveiculo = cc.idveiculo) 
                    where 
                    v.codentidade={cod_entidade}""",
'EstornoConsumo' : f"""select 
                ec.codentidade ||'|'||
                ec.nrsequencial ||'|'||
                c.CODENTIDADE ||'|'||
                c.nrsequencial ||'|'||
                v.nrfrota ||'|'||
                LPAD( EXTRACT( day FROM ec.DATAESTORNO), 2, '0' ) ||'/'|| LPAD( EXTRACT( month FROM ec.DATAESTORNO), 2, '0' ) ||'/'|| LPAD( EXTRACT( YEAR FROM ec.DATAESTORNO), 4, '0' ) ||'|'||
                ec.MES ||'|'||
                ec.ANO ||'|'||
                ec.MOTIVO ||'|'||
                replace(ec.NRQUANTIDADE, '.', ',') ||'|' as extractEstornoConsumo
                from 
                scf_estornoconsumocombustivel ec 
                join scf_consumocombustivel c on (c.idconsumocombustivel = ec.idconsumocombustivel) 
                join scf_veiculo v on (v.idveiculo = c.idveiculo) 
                where 
                ec.codentidade={cod_entidade}""",
'ControleSimAm' : f"""select 
                v.codentidade ||'|'||
                v.nrfrota ||'|'||
                vcs.CDCONTROLE ||'|'||
                vcs.CDTIPOLANCAMENTO ||'|'||
                LPAD( EXTRACT( day FROM vcs.DTLANCAMENTO ), 2, '0' ) ||'/'|| LPAD( EXTRACT( month FROM vcs.DTLANCAMENTO ), 2, '0' ) ||'/'|| LPAD( EXTRACT( YEAR FROM vcs.DTLANCAMENTO ), 4, '0' ) ||'|'||
                vcs.VLRDECLARADO ||'|'||
                coalesce(vcs.DSNOTAEXPLICATIVA, '') ||'|'||
                vcs.CDCONTROLESIMAM ||'|'||
                vcs.ISTROCAACUMULADOR ||'|'||
                replace(vcs.VLRACUMULADORINICIAL, '.', ',') ||'|'||
                replace(vcs.VLRACUMULADORFINAL, '.', ',') ||'|'||
                replace(vcs.NOVOVALORACUMULADORINICIAL, '.', ',') ||'|'|| 
                coalesce(va.dtleituraacumulador,'') ||'|' as ExtractControleSimAm
                from 
                scf_veiculocontrolesimam vcs 
                join scf_veiculo v on (v.idveiculo = vcs.idveiculo) 
                left join scf_veiculoacumulador va on (va.idveiculoacumulador = vcs.idveiculoacumulador) 
                where 
                v.codentidade={cod_entidade} """,
'OrdemAbastecimento' : f"""select
                oa.codentidade ||'|'||
                oa.NRORDEMABASTECIMENTO ||'|'||
                v.nrfrota ||'|'|| 
                oa.CODFORNECEDOR ||'|'||
                m.nrcodigomotorista ||'|'||
                LPAD( EXTRACT( day FROM oa.DTORDEMABASTECIMENTO), 2, '0' ) ||'/'|| LPAD( EXTRACT( month FROM oa.DTORDEMABASTECIMENTO), 2, '0' ) ||'/'|| LPAD( EXTRACT( YEAR FROM oa.DTORDEMABASTECIMENTO), 4, '0' ) ||'|'||
                p.codproduto ||'|'||
                oa.TPABASTECIMENTO ||'|'||
                replace(oa.NRLITROSORDEMABASTECIMENTO, '.',',') ||'|'||
                coalesce(va.NRABASTECIMENTO, '') ||'|'||
                oa.EXERCICIOLICITACAO ||'|'||
                oa.CODTIPOLICITACAO ||'|'||
                oa.CODLICITACAO ||'|'||
                replace(oa.NRSALDOLICITACAO, '.',',') ||'|'||
                coalesce(oa.CODPESSOA, '') ||'|'||
                coalesce(oa.CODLOCAL, '') ||'|'||
                oa.DSOBSERVACAO ||'|'||
                coalesce(oa.TEMPVLACUMULADOR, '') ||'|'||
                replace(coalesce(oa.VLACUMULADOR, ''), '.',',') ||'|' as ExtractOrdemAbastecimento
                from 
                scf_ordemabastecimento oa 
                join scf_veiculo v on (v.idveiculo = oa.idveiculo) 
                left join scf_motorista m on (m.idmotorista = oa.idmotorista) 
                left join scf_produto p on (p.idproduto = oa.idproduto) 
                left join scf_veiculoabastecimento va on (va.idveiculoabastecimento = oa.idveiculoabastecimento) 
                where 
                oa.codentidade={cod_entidade}""",
'ClassificacaoFornecedor' : f""" select 
                cf.CODENTIDADE ||'|'||
                cf.CODFORNECEDOR ||'|'||
                cf.TPCLASSIFICACAOFORNECEDOR ||'|' as extractclassificacaoFornecedor 
                from 
                scf_classificacaofornecedor cf 
                where 
                cf.codentidade={cod_entidade}""",
'VeiculoOrdemServico' : f"""select
                        os.codentidade ||'|'||
                        os.NRORDEMSERVICO ||'|'||
                        v.nrfrota ||'|'||
                        os.CODFORNECEDOR ||'|'|| 
                        ts.nmtiposervico ||'|'||
                        LPAD( EXTRACT( day FROM os.DTORDEMSERVICO), 2, '0' ) ||'/'|| LPAD( EXTRACT( month FROM os.DTORDEMSERVICO), 2, '0' ) ||'/'|| LPAD( EXTRACT( YEAR FROM os.DTORDEMSERVICO), 4, '0' ) ||'|'||
                        LPAD( EXTRACT( day FROM os.DTINICIOORDEMSERVICO), 2, '0' ) ||'/'|| LPAD( EXTRACT( month FROM os.DTINICIOORDEMSERVICO), 2, '0' ) ||'/'|| LPAD( EXTRACT( YEAR FROM os.DTINICIOORDEMSERVICO), 4, '0' ) ||' '|| LPAD( EXTRACT( hour FROM os.DTINICIOORDEMSERVICO), 2, '0' ) ||':'|| LPAD( EXTRACT( minute FROM os.DTINICIOORDEMSERVICO), 2, '0' ) ||':'|| replace(LPAD( EXTRACT( second FROM os.DTINICIOORDEMSERVICO), 2, '0' ), '.', '0') ||'|'||
                        LPAD( EXTRACT( day FROM vai.dtleituraacumulador), 2, '0' ) ||'/'|| LPAD( EXTRACT( month FROM vai.dtleituraacumulador), 2, '0' ) ||'/'|| LPAD( EXTRACT( YEAR FROM vai.dtleituraacumulador), 4, '0' ) ||' '|| LPAD( EXTRACT( hour FROM vai.dtleituraacumulador), 2, '0' ) ||':'|| LPAD( EXTRACT( minute FROM vai.dtleituraacumulador), 2, '0' ) ||':'|| replace(LPAD( EXTRACT( second FROM vai.dtleituraacumulador), 2, '0' ), '.', '0') ||'|'||
                        LPAD( EXTRACT( day FROM vaf.dtleituraacumulador), 2, '0' ) ||'/'|| LPAD( EXTRACT( month FROM vaf.dtleituraacumulador), 2, '0' ) ||'/'|| LPAD( EXTRACT( YEAR FROM vaf.dtleituraacumulador), 4, '0' ) ||' '|| LPAD( EXTRACT( hour FROM vaf.dtleituraacumulador), 2, '0' ) ||':'|| LPAD( EXTRACT( minute FROM vaf.dtleituraacumulador), 2, '0' ) ||':'|| replace(LPAD( EXTRACT( second FROM vaf.dtleituraacumulador), 2, '0' ), '.', '0') ||'|'|| 
                        LPAD( EXTRACT( day FROM os.DTTERMINOORDEMSERVICO), 2, '0' ) ||'/'|| LPAD( EXTRACT( month FROM os.DTTERMINOORDEMSERVICO), 2, '0' ) ||'/'|| LPAD( EXTRACT( YEAR FROM os.DTTERMINOORDEMSERVICO), 4, '0' ) ||' '|| LPAD( EXTRACT( hour FROM os.DTTERMINOORDEMSERVICO), 2, '0' ) ||':'|| LPAD( EXTRACT( minute FROM os.DTTERMINOORDEMSERVICO), 2, '0' ) ||':'|| replace(LPAD( EXTRACT( second FROM os.DTTERMINOORDEMSERVICO), 2, '0' ), '.', '0') ||'|'|| 
                        os.DSOBSERVACAOORDEMSERVICO ||'|'||
                        os.ISACUMULADORFUNCIONANDO ||'|'||
                        m.NRCODIGOMOTORISTA ||'|'||
                        os.CODPESSOA ||'|'||
                        Coalesce(os.NRDIASGARANTIA, '') ||'|'||
                        Coalesce(os.LOCALRESPONSAVEL, '') ||'|'||
                        Coalesce(os.ORGAORESPONSAVEL, '') ||'|'||
                        Coalesce(os.UNIDADERESPONSAVEL, '') ||'|'||
                        Coalesce(os.CODLOCAL,'') ||'|' as extractVeiculoOrdemServico
                        from 
                        scf_veiculoordemservico os 
                        join scf_veiculo v on (v.idveiculo = os.idveiculo) 
                        join scf_tiposervico ts on (ts.idtiposervico = os.idtiposervico) 
                        left join scf_veiculoacumulador vai on (vai.idveiculoacumulador = os.idveiculoacumuladorosinicio) 
                        left join scf_veiculoacumulador vaf on (vaf.idveiculoacumulador = os.idveiculoacumuladorostermino) 
                        left join scf_motorista m on (m.idmotorista = os.idmotorista) 
                        where 
                        os.codentidade={cod_entidade} """,
'VeiculoOrdemServicoProduto' : f"""select 
                            os.codentidade ||'|'|| 
                            os.nrordemservico ||'|'|| 
                            p.codproduto ||'|'||
                            replace(osp.VLQUANTIDADE,'.',',') ||'|'||
                            replace(osp.VLTOTAL,'.',',') ||'|'||
                            osp.NRSEQUENCIAPRODUTO ||'|'||
                            osp.DSOBSERVACAO ||'|'||
                            coalesce(osp.NRDIASGARANTIA,'') ||'|' as VeiculoOrdemServicoProduto 
                            from 
                            scf_veiculoordemservicoproduto osp 
                            join scf_veiculoordemservico os on (os.idveiculoordemservico = osp.idveiculoordemservico) 
                            join scf_produto p on (p.idproduto = osp.idproduto) 
                            where 
                            os.codentidade={cod_entidade} """,
'Nota' : f"""select 
            n.CODENTIDADE ||'|'||
            n.IDNF ||'|'||
            n.CODFORNECEDOR ||'|'||
            n.IDTIPODOCFISCAL ||'|'||
            n.IDTIPOSERIEDOCFISCAL ||'|'||
            n.NUMERONOTAABASTECIMENTO ||'|'||
            LPAD( EXTRACT( day FROM n.DATAEMISSAO), 2, '0' ) ||'/'|| LPAD( EXTRACT( month FROM n.DATAEMISSAO), 2, '0' ) ||'/'|| LPAD( EXTRACT( YEAR FROM n.DATAEMISSAO), 4, '0' ) ||' '|| LPAD( EXTRACT( hour FROM n.DATAEMISSAO), 2, '0' ) ||':'|| LPAD( EXTRACT( minute FROM n.DATAEMISSAO), 2, '0' ) ||':'|| replace(LPAD( EXTRACT( second FROM n.DATAEMISSAO), 2, '0' ), '.', '0') ||'|'||
            replace(n.VALORNOTAFISCAL, '.',',') ||'|'||
            n.PERMITEAJUSTEDEVALORES ||'|'||
            LPAD( EXTRACT( day FROM n.DATAINICIOFATURAMENTO), 2, '0' ) ||'/'|| LPAD( EXTRACT( month FROM n.DATAINICIOFATURAMENTO), 2, '0' ) ||'/'|| LPAD( EXTRACT( YEAR FROM n.DATAINICIOFATURAMENTO), 4, '0' ) ||' '|| LPAD( EXTRACT( hour FROM n.DATAINICIOFATURAMENTO), 2, '0' ) ||':'|| LPAD( EXTRACT( minute FROM n.DATAINICIOFATURAMENTO), 2, '0' ) ||':'|| replace(LPAD( EXTRACT( second FROM n.DATAINICIOFATURAMENTO), 2, '0' ), '.', '0') ||'|'||
            LPAD( EXTRACT( day FROM n.DATAFINALFATURAMENTO), 2, '0' ) ||'/'|| LPAD( EXTRACT( month FROM n.DATAFINALFATURAMENTO), 2, '0' ) ||'/'|| LPAD( EXTRACT( YEAR FROM n.DATAFINALFATURAMENTO), 4, '0' ) ||' '|| LPAD( EXTRACT( hour FROM n.DATAFINALFATURAMENTO), 2, '0' ) ||':'|| LPAD( EXTRACT( minute FROM n.DATAFINALFATURAMENTO), 2, '0' ) ||':'|| replace(LPAD( EXTRACT( second FROM n.DATAFINALFATURAMENTO), 2, '0' ), '.', '0') ||'|'||
            n.STATUSNFABASTECIMENTO ||'|'||
            n.PROCESSADO ||'|'||
            replace(n.VALORNOTAFISCALCALCULADO, '.',',') ||'|' as ExtractnotaFiscal
            from 
            scf_nf n """,

'NotaProduto' : f"""select
                n.CODENTIDADE ||'|'||
                p.CODPRODUTO ||'|'||
                n.IDNF ||'|'||
                n.CODFORNECEDOR ||'|'||
                n.IDTIPODOCFISCAL ||'|'||
                n.IDTIPOSERIEDOCFISCAL ||'|'||
                n.NUMERONOTAABASTECIMENTO ||'|'||
                coalesce(replace(np.PRECOAJUSTADO, '.',','), '') ||'|' as notaProduto
                from Scf_NfProduto np
                join SCF_NF n on (n.IDNF = np.IDNF)
                left join SCF_PRODUTO p on (p.IDPRODUTO = np.IDPRODUTO)
                where
                n.CODENTIDADE={cod_entidade} """,
'NotaAbastecimento' : f"""select 
                v.CODENTIDADE ||'|'||
                v.NRFROTA ||'|'||
                va.NRABASTECIMENTO ||'|'||
                n.IDNF ||'|'||
                n.CODFORNECEDOR ||'|'||
                n.IDTIPODOCFISCAL ||'|'||
                n.IDTIPOSERIEDOCFISCAL ||'|'||
                n.NUMERONOTAABASTECIMENTO ||'|'||
                coalesce(replace(na.VALORLITROAJUSTADO, '.',','),'') ||'|'||
                coalesce(replace(na.VALORTOTALAJUSTADO, '.',','),'') ||'|' as notaAbastecimento
                from 
                Scf_NfAbastecimento na
                join SCF_VEICULOABASTECIMENTO va on (va.IDVEICULOABASTECIMENTO = na.IDVEICULOABASTECIMENTO)
                join scf_veiculo v on (v.IDVEICULO = va.IDVEICULO)
                left join SCF_NF n on (n.IDNF = na.IDNF)
                where
                v.CODENTIDADE={cod_entidade} """,

}