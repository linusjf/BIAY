# HOWTO #

## Add today's BIAY video ##

Execute the script `addvideo` with the following parameters:

video id - the id of the youtube video
day of year - 1 - 365/366
caption or title (in double quotes)

Example:

```
./addvideo tyuifg-fg 10 "Bible in a year"
```

Results:

1) Video id is appended to the videos.txt file in the root directory
2) Day010.md is generated in the January subdirectory
3) Day010.jpg image is generated in the January/jpgs directory
4) Day010.md file name is appended to the January/compact.txt file
5) January20XX.md file is updated (in the root directory) with the Day010.md contents
