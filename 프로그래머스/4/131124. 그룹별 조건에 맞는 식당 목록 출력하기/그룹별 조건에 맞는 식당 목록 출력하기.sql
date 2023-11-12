-- 코드를 입력하세요
SELECT
    M.MEMBER_NAME,
    R.REVIEW_TEXT,
    DATE_FORMAT(R.REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE
FROM
    REST_REVIEW AS R
LEFT JOIN
    MEMBER_PROFILE AS M
ON
    M.MEMBER_ID = R.MEMBER_ID
WHERE
    M.MEMBER_ID IN (
        SELECT
            MEMBER_ID
        FROM
            (SELECT
                MEMBER_ID,
                RANK() OVER (ORDER BY COUNT(*) DESC) AS RANKING
             FROM 
                REST_REVIEW
             GROUP BY
                MEMBER_ID
        ) AS D
        WHERE
            RANKING = 1
    )
ORDER BY
    R.REVIEW_DATE,
    R.REVIEW_TEXT;