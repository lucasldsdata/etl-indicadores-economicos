SELECT
    COUNT(*) AS total_registros,
    ROUND(AVG(valor)::numeric, 2) AS media_ipca,
    ROUND(MAX(valor)::numeric, 2) AS maior_ipca,
    ROUND(MIN(valor)::numeric, 2) AS menor_ipca
FROM public.ipca;

SELECT
    data,
    valor
FROM public.ipca
ORDER BY data;