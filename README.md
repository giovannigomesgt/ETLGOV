# ETLGOV
Fluxo ETL será dividido em:

1:a
Fazer o Download de tabelas individuais, extrair, renomear e enviar ao S3 disparar trigger para enviar dados para tratamento no EMR e carga no S3 disparar trigger para
executar este mesmo processo para as demais tabelas.

1:b
Fazer o Download de tabelas individuais, extrair, renomear e enviar ao S3, disparar trigger que repetirá este processo com as demais tabelas.
No final dispara trigger para realizar a transformação e carga de todas as tabelas.


Em ambas as tasks, será feito uma verificação do versionamento de datas dos arquivos no S3 e do arquivo no site do GOV
