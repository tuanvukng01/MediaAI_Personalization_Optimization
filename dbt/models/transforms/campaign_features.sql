with base as (
    select *, clicks/impressions as ctr
    from {{ ref('staging_campaigns') }}
)
select * from base