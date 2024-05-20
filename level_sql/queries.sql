--Query 1 : Segmenting Members Based on Activity Criteria

select 'High Engagement' as activity_criteria,count(*) from member where waiting_list_time < 10 and follow_reco_above_50p=True 
union
select 'Moderate Engagement' as activity_criteria,count(*) from member where (waiting_list_time >= 10 and waiting_list_time <= 20) or follow_reco_above_50p=False 
union
select 'Low Engagement' as activity_criteria,count(*) from member where waiting_list_time > 20  and follow_reco_above_50p=True;

--Query 2 : Analyzing Member Engagement
select member_id, created_at, follow_reco, 
sum(follow_reco) over (order by created_at rows between unbounded preceding and current row) rolling_average 
from member 
where follow_reco>75
order by created_at;


with last_three_records_members_with_reco_over_75 as (
select member_id, count(*) from member group by member_id having count(*) <= 3 and count(case when follow_reco > 75 then 1 end) > 0
)
select 
    m.member_id, 
    m.created_at,
    m.follow_reco as current_follow_reco,
    sum(m.follow_reco) over (order by m.created_at rows between unbounded preceding and current row) as rolling_average 
from last_three_records_members_with_reco_over_75 as filtered_member
inner join member m on m.member_id=filtered_member.member_id
order by m.member_id, m.created_at;