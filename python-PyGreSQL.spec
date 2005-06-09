Summary:	PostgreSQL module for Python
Summary(pl):	Modu³ PostgreSQL dla Pythona
Name:		python-PyGreSQL
Version:	3.6.2
Release:	1
License:	BSD-like
Group:		Libraries/Python
Source0:	ftp://ftp.pygresql.org/pub/distrib/PyGreSQL-%{version}.tgz
# Source0-md5:	1f2694ea546c852c5a0ba2b17f7c5ce1
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
%setup -q -n PyGreSQL-%{version}

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

find $RPM_BUILD_ROOT%{py_sitedir} -type f -name "*.py" -exec rm -rf {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Announce ChangeLog
%{py_sitedir}/*.py[co]
%attr(755,root,root) %{py_sitedir}/_pg.so
%{_examplesdir}/%{name}-%{version}
