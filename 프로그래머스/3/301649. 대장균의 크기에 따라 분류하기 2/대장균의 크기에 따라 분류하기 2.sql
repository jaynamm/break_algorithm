-- 코드를 작성해주세요

select 
    id, 
    case 
        when percent_rank() over (order by size_of_colony) >= 0.75 then 'CRITICAL'
        when percent_rank() over (order by size_of_colony) >= 0.5 then 'HIGH'
        when percent_rank() over (order by size_of_colony) >= 0.25 then 'MEDIUM'
        else 'LOW'
    end as colony_name
from ecoli_data
order by 1 asc