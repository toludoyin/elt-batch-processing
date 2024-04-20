
{{ 
    config(
        materialized='table'
    ) 
}}

select * from {{ref('stg_daily_stocks')}}