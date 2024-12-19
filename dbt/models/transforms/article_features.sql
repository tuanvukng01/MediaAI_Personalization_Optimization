with base as (
    select *,
    case when length > 1000 then 'long' else 'short' end as article_type
    from {{ ref('staging_articles') }}
)
select * from base