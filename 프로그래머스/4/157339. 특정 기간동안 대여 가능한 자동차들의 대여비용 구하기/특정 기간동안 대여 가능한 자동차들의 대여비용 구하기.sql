-- 코드를 입력하세요
SELECT
    DISTINCT C.CAR_ID,
    C.CAR_TYPE,
    FLOOR(C.DAILY_FEE * 30 * (100 - P.DISCOUNT_RATE) / 100) AS FEE
FROM
    CAR_RENTAL_COMPANY_CAR AS C
LEFT JOIN
    CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
ON
    C.CAR_ID = H.CAR_ID
LEFT JOIN
    (SELECT
        CAR_TYPE,
        DURATION_TYPE,
        DISCOUNT_RATE
     FROM
        CAR_RENTAL_COMPANY_DISCOUNT_PLAN
     WHERE
        DURATION_TYPE = "30일 이상"
    ) AS P
ON
    P.CAR_TYPE = C.CAR_TYPE
WHERE
    C.CAR_ID NOT IN (
        SELECT
            CAR_ID
        FROM
            CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE
            (START_DATE <= "2022-11-01" AND
            END_DATE >= "2022-11-30") OR
            (START_DATE BETWEEN "2022-11-01" AND "2022-11-30") OR
            (END_DATE BETWEEN "2022-11-01" AND "2022-11-30")
    ) AND
    C.CAR_TYPE IN ("세단", "SUV") AND
    (C.DAILY_FEE * 30 * (100 - P.DISCOUNT_RATE) / 100) BETWEEN 500000 AND 2000000
ORDER BY
    FEE DESC,
    C.CAR_TYPE,
    C.CAR_ID DESC