-- 1.Who worked on X song?

SELECT DISTINCT StaffName FROM Worked WHERE SongTitle = 'Tell Me Why';

-- OUTPUT:
-- Liz Rose
-- Nathan Chapman
--Taylor Swift



-- 2.What projects was Taylor involved with since X to Y?

SELECT Title FROM Song WHERE ReleaseDate >= '2007-09-01T00:00:00' AND ReleaseDate <= '2008-10-21T00:00:00';

-- OUTPUT:
-- I'm Only Me When I'm With You
-- Invisible
-- A Perfectly Good Heart
-- Fearless
-- Love Story
-- Breathe (Ft. Colbie Caillat)
-- Change
-- Last Christmas
-- Christmases When You Were Mine
-- Santa Baby
-- Silent Night
-- Christmas Must Be Something More
-- White Christmas
-- Best Days of Your Life
-- Picture to Burn (Rhapsody Version)
-- Umbrella (Live from SoHo)



-- 3.In what albums is the song X featured?

SELECT AlbumTitle FROM IsFeaturedIn WHERE SongTitle = 'The Last Time (Ft. Gary Lightbody)';

-- OUTPUT:
-- Red (Deluxe Version)



-- 4.What are the lyrics of song X?

SELECT Lyrics FROM Song WHERE Title = 'End Game (Ft. Ed Sheeran & Future)';
-- OUTPUT:
--'[Chorus: Taylor Swift, ', 'Future', ']', 'I wanna be your end game', ... 'I wanna be your end game, end game']
-- NOTE: Omitted part of the output for brevity's sake



-- 5.What songs DON'T belong to any album?

SELECT SongTitle FROM IsCategorizedAs WHERE CategoryName = 'Non-Album Songs';

-- OUTPUT:
-- Christmas Tree Farm
-- Carolina
-- Eyes Open (Taylor's Version)
-- Safe & Sound (Taylor's Version) by Taylor Swift, Joy Williams & John Paul White
-- If This Was a Movie (Taylor's Version)
-- All Of The Girls You Loved Before
-- Last Christmas
-- Christmases When You Were Mine
-- Santa Baby
-- Silent Night
-- Christmas Must Be Something More
-- White Christmas
-- Beautiful Ghosts
-- Crazier
-- You’ll Always Find Your Way Back Home
-- I Don’t Wanna Live Forever
-- This Is What You Came For
-- Only The Young
-- Eyes Open
-- Safe & Sound
-- Sweeter Than Fiction
-- Ronan
-- Today Was a Fairytale
-- Drops of Jupiter (Live/2011)
-- Bette Davis Eyes (Live/2011)
-- I Want You Back (Live/2011)
-- Breathless
-- Macavity
-- September (Recorded at The Tracking Room Nashville)
-- Umbrella (Live from SoHo)
-- Baby Don’t You Break My Heart Slow
-- American Girl



-- 6.What non-Taylor songs feature Taylor?

SELECT SongTitle FROM IsCategorizedAs WHERE CategoryName = 'Other Artist Songs';

-- OUTPUT:
-- Two Is Better Than One
-- The Alcott
-- Birch
-- Renegade
-- Bein’ With My Baby
-- Best Days of Your Life
-- Better Man
-- Babe
-- Highway Don’t Care
-- Half of My Heart
-- Gasoline (Remix)
-- Both of Us
-- The Joker And The Queen (Remix)
-- Hold On (Live)
-- Big Star (Live)
-- us.



-- 7.What are the 5 most visited song pages?

SELECT Title FROM Song
ORDER BY pageViews DESC
LIMIT 5;

-- OUTPUT:
-- All Too Well (10 Minute Version) (Taylor's Version) [From The Vault]
-- Fortnight (Ft. Post Malone)
-- cardigan
-- exile (Ft. Bon Iver)
-- So Long, London



-- 8.Which songs were written by Liz Rose and produced by Nathan Chapman?

SELECT SongTitle
FROM Worked
WHERE StaffName = 'Liz Rose'
AND JobTitle = 'Writer'

INTERSECT

SELECT SongTitle
FROM Worked
WHERE StaffName = 'Nathan Chapman'
AND JobTitle = 'Producer';

-- OUTPUT:
-- All Too Well
-- Christmases When You Were Mine
-- Cold as You
-- Come In With the Rain
-- Fearless
-- Mary's Song (Oh My My My)
-- Picture to Burn
-- Picture to Burn (Rhapsody Version)
-- Stay Beautiful
-- SuperStar
-- Teardrops On My Guitar
-- Tell Me Why
-- Tied Together with a Smile
-- Tim McGraw
-- White Horse
-- You Belong With Me

-- 9.What is that song that goes...?
-- NOTE: Doesn't work over lyrics spread over lines

SELECT Title
FROM Song
WHERE Lyrics like '%like a violin%';

-- OUTPUT:
-- I Did Something Bad



-- 10.What songs were produced by X?

SELECT SongTitle
FROM Worked
WHERE JobTitle = 'Producer'
AND StaffName = 'Jack Antonoff';

-- OUTPUT:
-- Mr. Perfectly Fine (Taylor's Version) [From the Vault]
-- That's When (Taylor's Version) [From the Vault] (Ft. Keith Urban)
-- Don't You (Taylor's Version) [From the Vault]
-- ...
-- Lover (Remix)
-- Sweeter Than Fiction
-- Anti-Hero (Remix)
-- us.

-- NOTE: Omitted part of the output for brevity's sake
