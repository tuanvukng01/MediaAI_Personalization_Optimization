with base as (
    select up.*, d.age as user_age, d.gender as user_gender, d.location
    from {{ ref('staging_user_profiles') }} up
    left join {{ ref('staging_demographics') }} d on up.user_id = d.user_id
)
select * from base