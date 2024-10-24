"""Query the database"""

import os
from databricks import sql
from dotenv import load_dotenv

complex_query = """
SELECT 
    CASE 
        WHEN w.major IS NOT NULL THEN 'STEM'  
        ELSE 'Non-STEM'                        
    END AS field_type, 
    COUNT(DISTINCT r.major) AS number_of_majors,      
    AVG(r.sharewomen) AS avg_share_women,             
    AVG(r.median) AS avg_median_salary,               
    SUM(r.employed) AS total_employed,                
    SUM(r.unemployed) AS total_unemployed,            
    AVG(r.unemployment_rate) AS avg_unemployment_rate 
FROM recent_grads r
LEFT JOIN women_stem w
ON r.major_code = w.major_code                       
GROUP BY field_type                                
ORDER BY avg_median_salary DESC; 
"""


def query():
    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("ACCESS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(complex_query)
            result = cursor.fetchall()

            for row in result:
                print(row)

            cursor.close()
            connection.close()

        return "Query successful!"


if __name__ == "__main__":
    query()
