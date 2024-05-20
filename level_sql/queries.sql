--Query 1 : Segmenting Members Based on Activity Criteria

SELECT 'High Engagement' AS activity_criteria,count(*) FROM member WHERE waiting_list_time < 10 AND follow_reco_above_50p=True
UNION
SELECT 'Moderate Engagement' AS activity_criteria,count(*) FROM member WHERE (waiting_list_time >= 10 AND waiting_list_time <= 20) OR follow_reco_above_50p=False
UNION
SELECT 'Low Engagement' AS activity_criteria,count(*) FROM member WHERE waiting_list_time > 20  AND follow_reco_above_50p=True;


--Query 2 : Analyzing Member Engagement

WITH at_least_one_reco_above_75 AS (
    SELECT member_id, count(*)
    FROM member
    GROUP BY member_id
    HAVING COUNT(CASE WHEN follow_reco > 75 THEN 1 END) >= 1
)
SELECT
    m.member_id,
    m.created_at,
    m.follow_reco AS current_follow_reco,
    AVG(m.follow_reco) OVER (ORDER BY created_at ROWS BETWEEN 3 PRECEDING AND current ROW) AS rolling_average
FROM at_least_one_reco_above_75 AS filtered_member
INNER JOIN member m ON m.member_id=filtered_member.member_id
ORDER BY m.member_id, m.created_at;