
{{ config(
    materialized='view'
    ) 
}}

select 
cast(index as date) as issue_date,
cast(open as float) as open_value,
cast(high as float) as high,
cast(low as float) as low,
cast(close as float) as close_value,
cast(adjustedclose as float) as adjusted_close,
cast(volume as numeric) as volume,
cast(dividendamount as float) as dividend_amount,
cast(splitcoefficient as float) as split_coefficient
from {{ source('stocks_db', 'stocks') }}
order by index desc