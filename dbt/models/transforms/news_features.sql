with base as (
    select
        n.*,
        a.author,
        a.length,
        a.publish_date
    from {{ ref('staging_news') }} n
    left join {{ ref('staging_articles') }} a on n.article_id = a.article_id
)
select *,
case
    when category in ('politics','business') then 'serious'
    else 'general'
end as content_tone
from base