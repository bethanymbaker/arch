Given the following tables/dataframes:
- device (device_id, device_category)
- user (user_id, country)
- playback (date, user_id, device_id, title_id)
- title (title_id, title_name)

1. Number of monthly users that watched Stranger Things since 1/1/2019 sorted by year and month
Output format
year  month    cnt
2019  1    2000000
2019  2    3000000
...

select year(date) as year, month(date) as month, count(distinct p.user_id) as cnt from
playback p
join title t
on t.title_id = p.title_id
where lower(title_name) LIKE 'stranger things' and date >= '2019-01-01'
group by 1, 2
order by 1, 2

2. Number of accounts that watched Stranger Things on at least two different device categories


select year, month, count(user_id) as cnt
from (
select year(date) as year, month(date) as month, p.user_id as user_id, count(distinct device_category) as num_categories from
playback p
join title t
join device d
on d.device_id = p.device_id
on t.title_id = p.title_id
where lower(title_name) LIKE 'stranger things' and date >= '2019-01-01'
group by 1, 2, 3
) t
where num_categories > 2
group by 1, 2
order by 1, 2