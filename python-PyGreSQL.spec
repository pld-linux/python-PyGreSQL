Summary:	PostgreSQL module for Python
Summary(pl):	Modu³ PostgreSQL dla Pythona
Name:		python-PyGreSQL
Version:	3.4
%define	pre	pre021201
Release:	0.%{pre}.1
License:	BSD-like
Group:		Libraries/Python
Source0:	ftp://ftp.pygresql.org/pub/distrib/PyGreSQL-%{version}-%{pre}.tgz
# Source0-md5:	8448fa076c1c3724706dfa93f24efc51
URL:		http://www.pygresql.org/
BuildRequires:	postgresql-backend-devel
BuildRequires:	postgresql-devel
BuildRequires:	python-devel
%pyrequires_eq	python
Obsoletes:	python-postgresql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyGreSQL is a Python module that interfaces to a PostgreSQL database.
It embeds the PostgreSQL query library to allow easy use of the
powerful PostgreSQL features from a Python script.

%description -l pl
PyGreSQL to modu³ Pythona bêd±cy interfejsem do bazy danych
PostgreSQL. Osadza bibliotekê zapytañ PostgreSQL, aby umo¿liwiæ ³atwe
korzystanie z potê¿nych mo¿liwo¶ci PostgreSQL-a w skryptach Pythona.

%prep
%setup -q -n PyGreSQL-%{version}-%{pre}

%build
./setup.py build_ext \
	-I/usr/include/postgresql/server

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install tutorial/*.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Announce ChangeLog README
%{py_sitedir}/*.py[co]
%attr(755,root,root) %{py_sitedir}/_pg.so
%{_examplesdir}/%{name}-%{version}
