select sum(quantity) as total_quantity,DATEPART(WEEK, week) as week_number from Weekly_Orders_Report WHERE DATEPART(WEEK, week) BETWEEN 1 AND 13 GROUP BY 
    DATEPART(WEEK, week)
ORDER BY 
    week_number;