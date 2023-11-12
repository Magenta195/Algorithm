-- 코드를 입력하세요
SET @hour = 8;

SELECT
    (@hour := @hour + 1) AS HOUR,
    (SELECT
        COUNT(*)
     FROM 
        ANIMAL_OUTS
     WHERE
        @hour = HOUR(DATETIME)
    ) AS COUNT
FROM
    ANIMAL_OUTS
WHERE
    @hour < 19;