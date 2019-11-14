#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bashdb
Version  : 5.0.1.1.0
Release  : 12
URL      : https://sourceforge.net/projects/bashdb/files/bashdb/5.0-1.1.1/bashdb-5.0-1.1.0.tar.gz
Source0  : https://sourceforge.net/projects/bashdb/files/bashdb/5.0-1.1.1/bashdb-5.0-1.1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: bashdb-bin = %{version}-%{release}
Requires: bashdb-data = %{version}-%{release}
Requires: bashdb-info = %{version}-%{release}
Requires: bashdb-license = %{version}-%{release}
Requires: bashdb-man = %{version}-%{release}
BuildRequires : grep
BuildRequires : sed
BuildRequires : util-linux

%description
Here we have a debugger (*the* debugger?) for Bash 3.0 and higher.
The command syntax generally follows that of the
[zsh debugger ](https://github.com/rocky/zshdb) trepanning debuggers
and, more generally, GNU debugger *gdb*.

%package bin
Summary: bin components for the bashdb package.
Group: Binaries
Requires: bashdb-data = %{version}-%{release}
Requires: bashdb-license = %{version}-%{release}

%description bin
bin components for the bashdb package.


%package data
Summary: data components for the bashdb package.
Group: Data

%description data
data components for the bashdb package.


%package info
Summary: info components for the bashdb package.
Group: Default

%description info
info components for the bashdb package.


%package license
Summary: license components for the bashdb package.
Group: Default

%description license
license components for the bashdb package.


%package man
Summary: man components for the bashdb package.
Group: Default

%description man
man components for the bashdb package.


%prep
%setup -q -n bashdb-5.0-1.1.0
cd %{_builddir}/bashdb-5.0-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573775830
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1573775830
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bashdb
cp %{_builddir}/bashdb-5.0-1.1.0/COPYING %{buildroot}/usr/share/package-licenses/bashdb/74a8a6531a42e124df07ab5599aad63870fa0bd4
cp %{_builddir}/bashdb-5.0-1.1.0/command/show_sub/copying.sh %{buildroot}/usr/share/package-licenses/bashdb/52da88f0dbc63b238773202dded383bd8c0b3421
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bashdb

%files data
%defattr(-,root,root,-)
/usr/share/bashdb/bashdb-main.inc
/usr/share/bashdb/bashdb-part2.sh
/usr/share/bashdb/bashdb-trace
/usr/share/bashdb/command/action.sh
/usr/share/bashdb/command/alias.sh
/usr/share/bashdb/command/backtrace.sh
/usr/share/bashdb/command/break.sh
/usr/share/bashdb/command/clear.sh
/usr/share/bashdb/command/commands.sh
/usr/share/bashdb/command/complete.sh
/usr/share/bashdb/command/condition.sh
/usr/share/bashdb/command/continue.sh
/usr/share/bashdb/command/debug.sh
/usr/share/bashdb/command/delete.sh
/usr/share/bashdb/command/disable.sh
/usr/share/bashdb/command/display.sh
/usr/share/bashdb/command/down.sh
/usr/share/bashdb/command/edit.sh
/usr/share/bashdb/command/enable.sh
/usr/share/bashdb/command/eval.sh
/usr/share/bashdb/command/examine.sh
/usr/share/bashdb/command/export.sh
/usr/share/bashdb/command/file.sh
/usr/share/bashdb/command/finish.sh
/usr/share/bashdb/command/frame.sh
/usr/share/bashdb/command/handle.sh
/usr/share/bashdb/command/help.sh
/usr/share/bashdb/command/history.sh
/usr/share/bashdb/command/info.sh
/usr/share/bashdb/command/info_sub/args.sh
/usr/share/bashdb/command/info_sub/breakpoints.sh
/usr/share/bashdb/command/info_sub/display.sh
/usr/share/bashdb/command/info_sub/files.sh
/usr/share/bashdb/command/info_sub/functions.sh
/usr/share/bashdb/command/info_sub/handle.sh
/usr/share/bashdb/command/info_sub/line.sh
/usr/share/bashdb/command/info_sub/program.sh
/usr/share/bashdb/command/info_sub/signals.sh
/usr/share/bashdb/command/info_sub/source.sh
/usr/share/bashdb/command/info_sub/stack.sh
/usr/share/bashdb/command/info_sub/variables.sh
/usr/share/bashdb/command/info_sub/warranty.sh
/usr/share/bashdb/command/info_sub/watchpoints.sh
/usr/share/bashdb/command/kill.sh
/usr/share/bashdb/command/list.sh
/usr/share/bashdb/command/load.sh
/usr/share/bashdb/command/log.sh
/usr/share/bashdb/command/next.sh
/usr/share/bashdb/command/pwd.sh
/usr/share/bashdb/command/quit.sh
/usr/share/bashdb/command/return.sh
/usr/share/bashdb/command/run.sh
/usr/share/bashdb/command/search.sh
/usr/share/bashdb/command/set.sh
/usr/share/bashdb/command/set_sub/annotate.sh
/usr/share/bashdb/command/set_sub/args.sh
/usr/share/bashdb/command/set_sub/autoeval.sh
/usr/share/bashdb/command/set_sub/autolist.sh
/usr/share/bashdb/command/set_sub/basename.sh
/usr/share/bashdb/command/set_sub/debug.sh
/usr/share/bashdb/command/set_sub/debugging.sh
/usr/share/bashdb/command/set_sub/different.sh
/usr/share/bashdb/command/set_sub/dollar0.sh
/usr/share/bashdb/command/set_sub/editing.sh
/usr/share/bashdb/command/set_sub/highlight.sh
/usr/share/bashdb/command/set_sub/history.sh
/usr/share/bashdb/command/set_sub/linetrace.sh
/usr/share/bashdb/command/set_sub/listsize.sh
/usr/share/bashdb/command/set_sub/prompt.sh
/usr/share/bashdb/command/set_sub/showcommand.sh
/usr/share/bashdb/command/set_sub/style.sh
/usr/share/bashdb/command/set_sub/trace-commands.sh
/usr/share/bashdb/command/set_sub/tty.sh
/usr/share/bashdb/command/set_sub/width.sh
/usr/share/bashdb/command/shell.sh
/usr/share/bashdb/command/show.sh
/usr/share/bashdb/command/show_sub/alias.sh
/usr/share/bashdb/command/show_sub/annotate.sh
/usr/share/bashdb/command/show_sub/args.sh
/usr/share/bashdb/command/show_sub/autoeval.sh
/usr/share/bashdb/command/show_sub/autolist.sh
/usr/share/bashdb/command/show_sub/basename.sh
/usr/share/bashdb/command/show_sub/commands.sh
/usr/share/bashdb/command/show_sub/copying.sh
/usr/share/bashdb/command/show_sub/debug.sh
/usr/share/bashdb/command/show_sub/different.sh
/usr/share/bashdb/command/show_sub/directories.sh
/usr/share/bashdb/command/show_sub/editing.sh
/usr/share/bashdb/command/show_sub/highlight.sh
/usr/share/bashdb/command/show_sub/history.sh
/usr/share/bashdb/command/show_sub/listsize.sh
/usr/share/bashdb/command/show_sub/prompt.sh
/usr/share/bashdb/command/show_sub/style.sh
/usr/share/bashdb/command/show_sub/tty.sh
/usr/share/bashdb/command/show_sub/version.sh
/usr/share/bashdb/command/show_sub/warranty.sh
/usr/share/bashdb/command/show_sub/width.sh
/usr/share/bashdb/command/signal.sh
/usr/share/bashdb/command/skip.sh
/usr/share/bashdb/command/source.sh
/usr/share/bashdb/command/step.sh
/usr/share/bashdb/command/trace.sh
/usr/share/bashdb/command/tty.sh
/usr/share/bashdb/command/undisplay.sh
/usr/share/bashdb/command/untrace.sh
/usr/share/bashdb/command/up.sh
/usr/share/bashdb/command/watch.sh
/usr/share/bashdb/data/shell.sh
/usr/share/bashdb/dbg-main.sh
/usr/share/bashdb/dbg-set-d-vars.inc
/usr/share/bashdb/getopts_long.sh
/usr/share/bashdb/init/io.sh
/usr/share/bashdb/init/opts.sh
/usr/share/bashdb/init/pre.sh
/usr/share/bashdb/init/require.sh
/usr/share/bashdb/init/term-background.sh
/usr/share/bashdb/init/vars.sh
/usr/share/bashdb/lib/action.sh
/usr/share/bashdb/lib/alias.sh
/usr/share/bashdb/lib/break.sh
/usr/share/bashdb/lib/cmd-hooks.sh
/usr/share/bashdb/lib/columnize.sh
/usr/share/bashdb/lib/commands.sh
/usr/share/bashdb/lib/complete.sh
/usr/share/bashdb/lib/dbg-call.sh
/usr/share/bashdb/lib/display.sh
/usr/share/bashdb/lib/file.sh
/usr/share/bashdb/lib/filecache.sh
/usr/share/bashdb/lib/fns.sh
/usr/share/bashdb/lib/frame.sh
/usr/share/bashdb/lib/help.sh
/usr/share/bashdb/lib/hist.sh
/usr/share/bashdb/lib/hook.sh
/usr/share/bashdb/lib/info.sh
/usr/share/bashdb/lib/journal.sh
/usr/share/bashdb/lib/list.sh
/usr/share/bashdb/lib/msg.sh
/usr/share/bashdb/lib/processor.sh
/usr/share/bashdb/lib/run.sh
/usr/share/bashdb/lib/save-restore.sh
/usr/share/bashdb/lib/setshow.sh
/usr/share/bashdb/lib/shell.sh
/usr/share/bashdb/lib/sig.sh
/usr/share/bashdb/lib/sort.sh
/usr/share/bashdb/lib/stepping.sh
/usr/share/bashdb/lib/subcmd.sh
/usr/share/bashdb/lib/term-highlight.py
/usr/share/bashdb/lib/unescape.sh
/usr/share/bashdb/lib/validate.sh

%files info
%defattr(0644,root,root,0755)
/usr/share/info/bashdb.info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bashdb/52da88f0dbc63b238773202dded383bd8c0b3421
/usr/share/package-licenses/bashdb/74a8a6531a42e124df07ab5599aad63870fa0bd4

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/bashdb.1
