%define tarname sqlite-ruby
Summary:	SQLite module for Ruby
Summary(pl.UTF-8):	Moduł SQLite dla Ruby
Name:		ruby-sqlite
Version:	2.2.3
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/2819/%{tarname}-%{version}.tar.bz2
# Source0-md5:	b7bd0e31ee261014535f05deda704acf
URL:		http://sqlite-ruby.rubyforge.org
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	setup.rb = 3.3.1
BuildRequires:	sqlite-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SQLite module for Ruby.

%description -l pl.UTF-8
Moduł SQLite dla Ruby.

%prep
%setup -q -n %{tarname}-%{version}
cp %{_datadir}/setup.rb .

%build
echo sqlite_api.c > ext/MANIFEST
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_archdir}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_archdir}/*.so
%{ruby_rubylibdir}/sqlite.rb
%{ruby_rubylibdir}/sqlite
