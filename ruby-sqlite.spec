%define	ruby_sitearchdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_libdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define tarname sqlite-ruby
Summary:	SQLite module for Ruby
Summary(pl):	Modu³ SQLite dla Ruby
Name:		ruby-sqlite
Version:	1.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/%{tarname}/%{tarname}-%{version}.tar.gz
# Source0-md5:	cc22e5ce8b3ddcb3de27eb4d7eaa23bc
URL:		http://sqlite-ruby.sourceforge.net
BuildRequires:	ruby
BuildRequires:	sqlite-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SQLite module for Ruby.

%description -l pl
Modu³ SQLite dla Ruby.

%prep
%setup -q -n sqlite

%build
ruby extconf.rb
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_sitearchdir}

install _sqlite.so $RPM_BUILD_ROOT%{ruby_sitearchdir}
install lib/sqlite.rb $RPM_BUILD_ROOT%{ruby_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{ruby_sitearchdir}/*
%{ruby_libdir}/sqlite.rb
