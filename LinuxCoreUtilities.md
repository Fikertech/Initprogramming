		5 linux core utilities
	
1. RM

NAME
       rm - remove files or directories

SYNOPSIS
       rm [OPTION]... [FILE]...

DESCRIPTION
       This  manual  page documents the GNU version of rm.  rm removes each
       specified file.  By default, it does not remove directories.

       If the -I or --interactive=once option is given, and there are  more
       than  three  files  or the -r, -R, or --recursive are given, then rm
       prompts the user for whether to proceed with the  entire  operation.
       If the response is not affirmative, the entire command is aborted.

       Otherwise,  if  a  file is unwritable, standard input is a terminal,
       and the -f or --force option is not given, or the -i  or  --interac‐
       tive=always  option is given, rm prompts the user for whether to re‐
       move the file.  If the response is  not  affirmative,  the  file  is
       skipped.

OPTIONS
       Remove (unlink) the FILE(s).

2. MKTEMP

NAME
       mktemp - create a temporary file or directory

SYNOPSIS
       mktemp [OPTION]... [TEMPLATE]

DESCRIPTION
       Create  a  temporary  file or directory, safely, and print its name.
       TEMPLATE must contain at least 3 consecutive 'X's in last component.
       If  TEMPLATE  is  not specified, use tmp.XXXXXXXXXX, and --tmpdir is
       implied.  Files are created u+rw, and directories u+rwx, minus umask
       restrictions.

       -d, --directory
              create a directory, not a file

       -u, --dry-run
              do not create anything; merely print a name (unsafe)

       -q, --quiet
              suppress diagnostics about file/dir-creation failure

       --suffix=SUFF
              append SUFF to TEMPLATE; SUFF must not contain a slash.
              
 3. PR
 
 NAME
       pr - convert text files for printing

SYNOPSIS
       pr [OPTION]... [FILE]...

DESCRIPTION
       Paginate or columnate FILE(s) for printing.

       With no FILE, or when FILE is -, read standard input.

       Mandatory  arguments to long options are mandatory for short options
       too.

       +FIRST_PAGE[:LAST_PAGE], --pages=FIRST_PAGE[:LAST_PAGE]
              begin [stop] printing with page FIRST_[LAST_]PAGE

       -COLUMN, --columns=COLUMN
              output COLUMN columns and print columns down,  unless  -a  is
              used. Balance number of lines in the columns on each page

       -a, --across
              print  columns  across  rather  than down, used together with
              -COLUMN

4.  NOHUP

NAME
       nohup - run a command immune to hangups, with output to a non-tty

SYNOPSIS
       nohup COMMAND [ARG]...
       nohup OPTION

DESCRIPTION
       Run COMMAND, ignoring hangup signals.

       --help display this help and exit

       --version
              output version information and exit

       If  standard  input  is  a  terminal, redirect it from an unreadable
       file.  If standard output is  a  terminal,  append  output  to  'no‐
       hup.out'  if possible, '$HOME/nohup.out' otherwise.  If standard er‐
       ror is a terminal, redirect it to standard output.  To  save  output
       to FILE, use 'nohup COMMAND > FILE'.

       NOTE:  your  shell  may have its own version of nohup, which usually
       supersedes the version described here.  Please refer to your shell's
       documentation for details about the options it supports.

5. DD

NAME
       dd - convert and copy a file

SYNOPSIS
       dd [OPERAND]...
       dd OPTION

DESCRIPTION
       Copy a file, converting and formatting according to the operands.

       bs=BYTES
              read  and  write  up to BYTES bytes at a time (default: 512);
              overrides ibs and obs

       cbs=BYTES
              convert BYTES bytes at a time

       conv=CONVS
              convert the file as per the comma separated symbol list

       count=N
              copy only N input blocks

       ibs=BYTES

            
