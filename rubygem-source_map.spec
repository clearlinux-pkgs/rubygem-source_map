#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-source_map
Version  : 3.0.1
Release  : 7
URL      : https://rubygems.org/downloads/source_map-3.0.1.gem
Source0  : https://rubygems.org/downloads/source_map-3.0.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause MIT
BuildRequires : ruby
BuildRequires : rubygem-json
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec

%description
The `source_map` gem provides an API for parsing, and an API for generating source maps in ruby.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n source_map-3.0.1
gem spec %{SOURCE0} -l --ruby > rubygem-source_map.gemspec

%build
gem build rubygem-source_map.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
source_map-3.0.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/source_map-3.0.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/source_map-3.0.1/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/source_map-3.0.1/README.md
/usr/lib64/ruby/gems/2.3.0/gems/source_map-3.0.1/lib/source_map.rb
/usr/lib64/ruby/gems/2.3.0/gems/source_map-3.0.1/lib/source_map/generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/source_map-3.0.1/lib/source_map/parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/source_map-3.0.1/lib/source_map/vlq.rb
/usr/lib64/ruby/gems/2.3.0/specifications/source_map-3.0.1.gemspec
