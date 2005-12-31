%define tarname sqlite-ruby
Summary:	SQLite module for Ruby
Summary(pl):	Modu³ SQLite dla Ruby
Name:		ruby-sqlite
Version:	1.0
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/%{tarname}/%{tarname}-%{version}.tar.gz
# Source0-md5:	cc22e5ce8b3ddcb3de27eb4d7eaa23bc
URL:		http://sqlite-ruby.sourceforge.net
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	sqlite-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SQLite module for Ruby.

%description -l pl
Modu³ SQLite dla Ruby.

%prep
%setup -q -n sqlite

%build
ruby extconf.rb
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

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
%attr(755,root,root) %{ruby_sitearchdir}/*
%{ruby_libdir}/sqlite.rb
