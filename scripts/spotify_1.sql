
track_metadata
+----------+---------------+----------------------+
| track_id |  artist_name  |      track_name      |
+----------+---------------+----------------------+
| P6a3w    | Drake         | In My Feelings       |
| PrVwa    | DJ Khaled     | No Brainer           |
| Il8iu    | Ariana Grande | no tears left to cry |
| ...      | ...           | ...                  |
+----------+---------------+----------------------+



user_track_streams

+------------+---------+----------+-----------+
|    date    | user_id | track_id | ms_played |
+------------+---------+----------+-----------+
| 2018-06-01 | fgylfg  | gkejg    |     63000 |
| 2018-06-01 | qwiufh  | jwhhk    |    486000 |
| 2018-06-01 | seoihg  | bhapq    |      2259 |
| ...        | ...     | ...      |       ... |
+------------+---------+----------+-----------+

user_metadata
+---------+------------+
| user_id | join_date  |
+---------+------------+
| fgylfg  | 2016-06-03 |
| qwiufh  | 2017-05-01 |
| seoihg  | 2018-05-20 |
| ...     | ...        |
+---------+------------+



# Write a query to find the name of the track which was played most often on February 12th this year.

select track_name from (
select track_name, artist_name, count(*)
from track_metadata tm
join user_track_streams uts
on tm.track_id = uts.track_id
where date = '2020-02-12'
group by 1, 2
order by 3 desc )
limit 1


# For each track, pull the day the track had its most streams.
# track 1.  jan 19
# track 2   mar 4


select s.date, t.track_id, max(kount) as max_count
from (
select date, track_id, count(*) as kount
from user_track_streams
group by 1, 2
) t
join
(
select date, track_id, count(*) as kount
from user_track_streams
group by 1, 2
) s
where s.track_id = t.track_id and s.kount = t.max_count



# What is the track that is played by the most unique users on their first day on Spotify?

select uts.track_id, count(distinct um.user_id) as num_users
from (
select um.user_id, um.join_date, uts.track_id
from user_metadata um
join user_track_streams uts
on uts.user_id = um.user_id and uts.date = um.join_date
) t
group by 1
sort by 2 desc
limit 1