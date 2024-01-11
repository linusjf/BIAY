# HOWTO #

<!-- vim-markdown-toc GFM -->

* [Prerequisites](#prerequisites)
* [Add today\'s Youtube video](#add-todays-youtube-video)
* [Add today\'s sharing](#add-todays-sharing)
* [Generate markdown for Youtube video](#generate-markdown-for-youtube-video)
* [Merge monthly markdown files into one large README](#merge-monthly-markdown-files-into-one-large-readme)

<!-- vim-markdown-toc -->

## Prerequisites ##

+ [convert](https://imagemagick.org/index.php)
+ [curl](https://curl.se/)
+ [gm](http://www.graphicsmagick.org/)
+ [m4](https://www.gnu.org/software/m4/)
+ [markdown-toc](https://github.com/jonschlinkert/markdown-toc)
+ [stitchmd](https://github.com/abhinav/stitchmd)

Create a directory for each month of the year under the root directory.
Add a header.md file under each monthly directory with the following content.

Example for January:
```text
<!-- toc -->
# January 2024 #
BIAY January 2024
```

The `<!-- toc -->` comment header is mandatory else markdown-toc will not generate the table of contents
for the monthly markdown (in this case, January2024.md).

You can replace the top-level header with your own if you wish.

## Add today\'s Youtube video ##

Execute the script `addvideo` with the following parameters:

+ video id - the id of the youtube video
+ day of year - 1 - 365/366
+ caption or title (in double quotes)

Example:

```bash
./addvideo 5I2BbalTOPo 10 "Hagar and Ishmael"
```

Results:

1) Video id is appended to the videos.txt file in the root directory.
2) Day010.md is generated in the January subdirectory.
3) Day010.jpg image is generated in the January/jpgs directory.
4) Day010.md file name is appended to the January/compact.txt file.
5) January20XX.md file is updated (in the root directory) with the Day010.md contents.

## Add today\'s sharing ##

1) First, add today's video.
2) Edit the generated Dayxxx.md file for today.
3) Paste the sharing text into the file adding appropriate markdown headers as needed.
4) Save the file.
5) Execute script `genmonth` with the following parameters:
+ month index - 1 - 12
+ four digit year - 20XX

    Example:
    ```bash
    ./genmonth 01 2024
    ```

    Results:

    - The January2024.md file is updated with the sharing text added to the Day010.md file.

You can add sharing to other days as well in a similar fashion.
Don't forget to execute `genmonth` with the appropriate month index for that day.

## Generate markdown for Youtube video ##

Execute the `genvidmd` script with the following parameters:

- vid - video id
- caption - video title
- pathtoimg - relative path to jpeg image file to be generated

Example:
```bash
./genvidmd g7o7WjQc3as "Bringing the Bible back to Catholics" January/jpgs/bringingback.jpg
```

Results:
1) The markdown is generated on the command line. This can be used to insert video markdown in your markdown files.
2) The overlaid image file for the video is generated as January/jpgs/bringingback.jpg.


## Merge monthly markdown files into one large README ##

1) Edit the stitch.md file provided to include the markdown files you wish to merge.

2) The file format is as follows:
    ```markdown
    # README
    - [BIAY](redme.md)
    - [January 2024](January2024.md)
    - [February 2024](February2024.md)
    - [March 2024](March2024.md)
    - [April 2024](April2024.md)
    - [May 2024](May2024.md)
    - [June 2024](June2024.md)
    - [July 2024](July2024.md)
    - [August 2024](August2024.md)
    - [September 2024](September2024.md)
    - [October 2024](October2024.md)
    - [November 2024](November2024.md)
    - [December 2024](December2024.md)
    ```
    Include or exclude any files you need or don't need.

3) Execute the `stitch` script.

```bash
./stitch
```

Results:

A huge README is generated with all the contents of the listed markdown files in stitch.md.
